#DFS graph의 노드당 인접 노드가 배열로 주어질 때 방문 순서 프린트

#깊이탐색
def dfs(graph, v, visited):
    visited[v]=True #현재노드 방문처리
    print(v,end='')#탐색순서 출력
    for i in graph[v]: #현재 노드와 연결된 다른 노드들 방문
        if not visited[i]:
            dfs(graph,i,visited)

#노드표현: 2차원리스트
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9
dfs(graph,1,visited)

