# https://www.acmicpc.net/problem/16954
from collections import deque
input = __import__('sys').stdin.readline
n=8

g=[list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

#상하좌우/대각선/정지
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]


que=deque()
que.append((7,0))
visited[7][0]=True
ans=0

#큐가 빌 때까지 반복
while que:
  x,y=que.popleft()
  #벽인경우 무시
  if g[x][y]=='#':
    continue

  #BFS소스코드 구현
  for i in range(len(dx)+1):
    nx=x+dx[i]
    ny=y+dy[i]
    #공간 벗어난 경우 무시
    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    #벽인 경우 무시
    if g[nx][ny]=='#':
      continue
    if nx==0:
      ans=1
      
    #처음 방문하는 경우
    if not visited[nx-1][ny]:
      visited[nx-1][ny]=True
      que.append((nx-1,ny))
  
print(ans)



# from collections import deque
# input = __import__('sys').stdin.readline
# n,m=8,8

# g=[list(input().strip()) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]

# #상하좌우/대각선/정지
# dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
# dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

# def bfs(x,y):
#     que=deque()
#     que.append((x,y))
#     visited[x][y]=True
#     ans=0
    
#     #큐가 빌 때까지 반복
#     while que:
#         x,y=que.popleft()
#         #벽인경우 무시
#         if g[x][y]=='#':
#           continue

#         #BFS소스코드 구현
#         for i in range(len(dx)+1):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             #공간 벗어난 경우 무시
#             if nx<0 or ny<0 or nx>=n or ny>=m:
#                 continue
#             #벽인 경우 무시
#             if g[nx][ny]=='#':
#                 continue
#             if nx==0:
#               ans=1
              
#             #처음 방문하는 경우
#             if not visited[nx-1][ny]:
#               visited[nx-1][ny]=True
#               que.append((nx-1,ny))
    
#     return ans

# print(bfs(7,0))