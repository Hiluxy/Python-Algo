from collections import deque

def bfs(g,x,y):
    que=deque()
    que.append((x,y))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    n=len(g)
    visited=[[False]*n for _ in range(n)]
    eat=0
    size=2
    move=0
    while que:
        x,y=que.popleft()
        #4방향
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #이동 가능 
            if 0<=nx<n and 0<=ny<n and size>=g[nx][ny]:#진짜 이동 가능한 경우
                visited[nx][ny]=True
                que.append((nx,ny))
                move+=1
                print(que)
                #물고기를 먹으면
                if size>g[nx][ny] and g[nx][ny]!=0:
                    eat+=1
                    #사이즈업
                    if eat==size:
                        size+=1
                        eat=0
                        #그래프 내에 내가 먹을 수 있는 물고기가 하나라도 있으면 go, 아니면 빠져나오기 (탐색 다 했는지 확인)
                        if isFish(g,size)==True and visited==True:
                            continue
                        else:
                            return move
    return move


def isFish(g,size):
    global n
    for i in range(n):
        for j in range(n):
            if g[i][j]<=size and g[i][j]!=0:
                return True
    return False

def isVisited(visited):
    global n
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                False
    True
    
        

n=int(input())
g=[]
for _ in range(n):
    g.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(n):
        if g[i][j]==9:
            x,y=i,j
            break

print(bfs(g,x,y))