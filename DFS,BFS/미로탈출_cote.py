# 🔶교재: 이것이 코딩 테스트다 with 파이썬 - 나동빈
# Chapter  5 DFS/BFS
# 실전문제 5-4 미로 탈출 152p

from collections import deque

n,m=map(int,input().split())
g=[]
for i in range(n):
    g.append(list(map(int,input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    que=deque()
    que.append((x,y))
    
    #큐가 빌 때까지 반복
    while que:
        x,y=que.popleft()

        #BFS소스코드 구현
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #공간 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            #0인 경우 무시
            if g[nx][ny]==0:
                continue
            #처음 방문하는 경우
            if g[nx][ny]==1:
                g[nx][ny]=g[x][y]+1
                que.append((nx,ny))

    return g[n-1][m-1]

print(bfs(0,0))
