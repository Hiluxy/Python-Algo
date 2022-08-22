# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 
# 예제 입력 1 
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
# 예제 출력 1 
# 5

import sys 
sys.setrecursionlimit(20000)

n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]

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
  #graph는 0으로 초기화한 후 h이하만 1로
  graph = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if g[i][j]<=h:
        graph[i][j]=1
  #모든 노드(위치)에 대하여 채우기(0으로 이어진부분 개수 세기)
  result=0
  for i in range(n):
      for j in range(n):
          if dfs(i,j)==True:
              result+=1
  num_max=max(num_max,result)

print(num_max)
