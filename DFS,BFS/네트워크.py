'''
입력값 〉	3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
기댓값 〉	2
입력값 〉	3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
기댓값 〉	1
'''

from collections import deque


def solution(n, computers):
    visited = [False] * n
    # 정의된 BFS 함수 호출
    answer=bfs(computers, 0, visited)
    return answer

# BFS 함수 정의
def bfs(graph, vv, visited):
    cnt=0
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([vv])
    # 현재 노드를 방문 처리
    visited[vv] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]: #graph[v]=[1, 1, 0]
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            else:
                cnt+=1
    
    return cnt



def main():
    #print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    
if __name__ == '__main__':
    main()