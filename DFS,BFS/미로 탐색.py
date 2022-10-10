from collections import deque


def bfs(g,sx,sy):
    n=len(g)
    m=len(g[0])
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    que=deque()
    que.append((sx,sy))
    visited=[[False]*m for _ in range(m)]
    #큐가 빌 때까지 반복
    while que:
        x,y=que.popleft()
        #BFS소스코드 구현
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if g[nx][ny]==0:
                continue
            if g[nx][ny]==1 and visited[nx][ny]==False:
                g[nx][ny]=g[x][y]+1
                que.append((nx,ny))
                visited[nx][ny]=True
    return g[-1][-1]

if __name__ == "__main__":
    n,m=map(int,input().split())
    g=[]
    for i in range(n):
        g.append(list(map(int,input())))
    result=bfs(g,0,0)
    print(result)