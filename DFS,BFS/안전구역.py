
import sys 
sys.setrecursionlimit(10000)

# n=map(int,input().split())
# g=[list(map(int,input().split())) for _ in range(n)]


# g=[]
# for i in range(n):
#     g.append(list(map(int,input())))

# n=5
# g=[[6,8,2,6,2],
# [3,2,3,4,6],
# [6,7,3,3,2],
# [7,2,5,3,6],
# [8,9,5,2,7]]

n=7
g=[[9,9,9,9,9,9,9],
[9, 2, 1, 2, 1, 2, 9],
[9, 1, 8, 7, 8, 1, 9],
[9, 2, 7, 9, 7, 2, 9],
[9, 1, 8, 7, 8, 1, 9],
[9, 2, 1, 2, 1, 2, 9],
[9, 9, 9, 9, 9, 9, 9]]


def dfs(x,y):
    #범위를 벗어날 경우
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return False

	#방문하지 않았다면 1처리
    if graph[x][y]==0:
        graph[x][y]=1

		#상하좌우 재귀적 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True 
    return False

hmax=max(map(max, g))
num_max=0
for h in range(hmax):
  #graph부분 초기화 비어있는곳0, 채운곳1 
  graph = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if g[i][j]<=h:
        graph[i][j]=1
  #모든 노드(위치)에 대하여 채우기
  result=0
  for i in range(n):
      for j in range(n):
          if dfs(i,j)==True:
              result+=1
  num_max=max(num_max,result)

print(num_max)
