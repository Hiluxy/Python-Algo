
from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#graph=[[], [2, 3], [3, 4], [], []]
# 모든 도시에 대한 최단 거리 초기화
d = [-1] * (n + 1)
d[x] = 0 # 출발 도시까지의 거리는 0으로 설정

q=deque([x])
while q:
    now_node=q.popleft()
    #연결된 노드 꺼내기
    for next_node in graph[now_node]:
        #처음 방문하는 노드라면
        if d[next_node]==-1:
            #거리 갱신하고 큐에 넣기
            d[next_node]=d[now_node]+1
            q.append(next_node)

#최단거리 k인 도시 출력
flag=False
for n in range(1,n+1):
    if d[n]==k:
        print(n)
        flag=True

if flag==False:
    print(-1)