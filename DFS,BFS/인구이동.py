from collections import deque
import math
import sys

n,l,r=map(int,input().split())
g=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# n,l,r=3,5,10
# g=[[10, 15, 20], [20, 30, 25], [40, 22, 10]]

dx=[-1,1,0,0]
dy=[0,0,-1,-1]

def bfs(x,y):
    que=deque()
    que.append((x,y))
    #초기화
    visit[x][y]=True
    union_idx=[(x,y)]
    sum=g[x][y] #연합인구수
    #que가 빌 때까지
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #공간 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            #이미 방문했을경우 무시
            if visit[nx][ny]:
                continue
            #인구차이 조건 해당될경우
            if  l<=abs(g[nx][ny]-g[x][y])<=r:
                visit[nx][ny]=True
                union_idx.append((nx,ny))
                sum+=g[nx][ny]
                que.append((nx,ny))
        
    for x,y in union_idx:
        g[x][y]=math.floor(sum/len(union_idx))
    
    return len(union_idx)

result=0
while True: #인구 이동 없을 때까지
    visit=[[False]*n for _ in range(n) ]
    check=False #인구 이동 있는지 check로 확인
    for i in range(n):
        for j in range(n):
            if not visit[i][j]: #방문하지 않았을경우 
                if bfs(i,j)>1:
                    check=True
    if not check: #인구 이동 없으면
        break
    result+=1

print(result)