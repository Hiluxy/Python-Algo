import sys
input = sys.stdin.readline

r,c,time= map(int, input().split())
board = [list(input().strip()) for _ in range(r)]


dx=[-1,1,0,0]
dy=[0,0,-1,1]


if time<=1:
    for l in board:
        print(''.join(l))
if time%2==0: #짝수시간 -> 전체가 폭탄
    for i in range(r):
        print('O'*c)
else:
    #ver.1 ->검정 범위 밖에 주황폭탄 있음
    #borad(초기)와 bomb1 비교
    bomb1=[['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):#검정폭탄+상하좌우 . 으로 만든다
            if board[y][x]=='O':
                bomb1[y][x]=='.'
            else :
                for i in range(4):
                    if 0<=y+dy[i]<r and 0<=x+dx[i]<c and board[y+dy[i]][x+dx[i]]=='O' :
                        bomb1[y][x]='.'
                        break
    
    #ver.2(이하 같음)
    #bomb1와 bomb2 비교
    bomb2=[['O']*c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if bomb1[y][x]=='O':
                bomb2[y][x]=='.'
            else:
                for i in range(4):
                    if 0<=y+dy[i]<r and 0<=x+dx[i]<c and bomb1[y+dy[i]][x+dx[i]]=='O':
                        bomb2[y][x]='.'
                        break
    
    if time%4==3: #3,7,9.. bom1출력
        for l in bomb1:
            print(''.join(l))
    if time%4==1: #5,9,13.. bom2출력
        for l in bomb2:
            print(''.join(l))