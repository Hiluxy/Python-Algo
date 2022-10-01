from collections import deque


def solution(maps):

def bfs(x,y,maps):
    n=len(maps)
    m=len(maps[0])    
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited = [[False] * m for i in range(n)]
    U_dic={}#영토 안 {A:3,B:5,,,}
    que=deque()
    que.append((x,y))#탐색하려는 좌표 담기
    while que:
        x,y=que.popleft()

        #탐색
        for i in range(4):
            nx=x+dx
            ny=y+dy
            #공간 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #.인 경우 무시
            if maps[nx][ny]=='.':
                visited[nx][ny]==True #방문처리
                continue   
            #처음 방문시
            if visited[nx][ny]==False:
                if 'A' in U_dic:
                    U_dic[maps[nx][ny]]+=1
                else:
                    U_dic[maps[nx][ny]]=1
    



'''테스트 1
입력값 〉
["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]
기댓값 〉
15
실행 결과 〉
실행한 결괏값 0이 기댓값 15과 다릅니다.
테스트 2
입력값 〉
["XY..", "YX..", "..YX", ".AXY"]
기댓값 〉
5
실행 결과 〉
실행한 결괏값 0이 기댓값 5과 다릅니다.'''