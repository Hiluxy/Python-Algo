'''
입력값 〉	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
기댓값 〉	11
입력값 〉	[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
기댓값 〉	-1
'''

from collections import deque
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solution(maps):
    return bfs(0,0,maps)

def bfs(x,y,g):
    n=len(g)
    m=len(g[0])
    visited = [[False] * m for i in range(n)]
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
                visited[nx][ny]=True

    if visited[n-1][m-1]==False:
        return -1
    else:
        return g[n-1][m-1]


maps=[[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
print(solution(maps))     

