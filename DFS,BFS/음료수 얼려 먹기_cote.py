# 🔶교재: 이것이 코딩 테스트다 with 파이썬 - 나동빈
# Chapter 5 DFS/BFS
# 실전문제 5-3 음료수 얼려 먹기 149p
#https://im-the-best-output.tistory.com/105?category=1289887

#비어있는곳0, 채운곳1 

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    #범위를 벗어날 경우
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False

	#방문하지 않았다면 1처리,재귀호출,True
    if graph[x][y]==0:
        graph[x][y]=1

		#상하좌우 재귀적 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True 
    return False

#모든 노드(위치)에 대하여 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)
