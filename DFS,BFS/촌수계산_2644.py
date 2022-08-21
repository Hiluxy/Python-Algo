def dfs(graph,v,visited):
    #현재 노드 방문처리
    visited[v]=True
    print(v,end=" ")
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



num=int(input())
a,b=map(int,input().split())
n=int(input())
visited=[False]*(num+1)
graph=[[] for _ in range(num+1)]
ans=[]

dfs(graph,7,0)

#방문안되면 
