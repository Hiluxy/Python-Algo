
for tc in range(int(input())):
    m,n,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    for i in range(k):
        y,x=map(int,input().split())
        graph[x][y]=1

    def dfs(x,y):
        #범위 벗어나면 f
        if x<=-1 or y<=-1 or x>=n or y>=m:
            return False

        #방문하지 않았다면 0처리
        if graph[x][y]==1:
            graph[x][y]=0

            #상하좌우 호출
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)  
            return True
        return False 

    result=0
    for i in range(n):
        for j in range(m):
            if dfs(i,j)==True:
                result+=1
    

    print(result)
