
from collections import deque

def bfs(graph,v,visited):
    queue=deque([v])
    visited[v]=True #현재노드 방문처리
    #큐가 빌때까지 반복
    while queue:
        now_v=queue.popleft()
        print(v,end=' ')
        #노드와 연결된(방문x)노드들 큐에 추가
        for i in graph[now_v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#노드표현: 2차원리스트
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited=[False]*9
bfs(graph,1,visited)

