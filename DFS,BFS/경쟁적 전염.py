from collections import deque


n,k=map(int, input().split())
graph=[] #전체 보드 정보
viruses=[] #바이러스 정보 (넘버,시간,x,y)
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    #보드 정보 한 줄씩 입력
    graph.append(list(map(int,input().split())))
    for j in range(n):
        #해당 위치 바이러스가 있음->바이러스 정보넣기
        if graph[i][j]!=0:
            viruses.append((graph[i][j],0,i,j))
targetS,targetX,targetY=map(int, input().split())

#정렬(낮은 번호 바이러스 먼저 증식)
viruses.sort()
q=deque(viruses)

#bfs
while q:
    num,s,x,y=q.popleft()
    if s==targetS:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #다음 위치로 이동 가능: 범위 안&비어있음
        if 0<=nx and 0<=ny and nx<n and ny<n:
            if graph[nx][ny]==0:
                graph[nx][ny]=num #바이러스 넣기
                q.append((num,s+1,nx,ny))

print(graph[targetX-1][targetY-1])

