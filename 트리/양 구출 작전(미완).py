# n=int(input())
# g=[[] for _ in range(n+1)] #연결 노드 저장
# sw_num=[[] for _ in range(n+1)] #[[] ['S',100]...]

# for i in range(n-1): #2번노드부터 n까지
#     a,b,c=map(str,input().split())
#     g[int(c)].append(i+2)
#     sw_num[i].append(a,int(b))

# print(sw_num)
# print(g)

# result=0
# def dfs(v):
#     for i in g[v]:#[2,3,4]
#         #양인 경우
#         if g[v][0]=='S':
#             result+=g[v][1]
#         #늑대인 경우
#         else:
#             result-=g[v][1]
#             if result<0:
#                 result=0

# dfs(1)
# print(result)

# 0. 입력받기
import sys
sys.setrecursionlimit(123458)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)] #[[], [2, 3, 4], [5, 6], [], [], [], [7], []]
node = [[], [0,0]] #[[], [0, 0], ['S', 100], ['S', 100], ['W', 100], ['S', 1000], ['W', 1000], ['S', 900]]

# 1. 트리구조 만들기
for i in range(N-1):
    kind, number, connection = input().split()
    tree[int(connection)].append(i+2)
    node.append([kind, int(number)])



# 2. dfs를 이용하여 탐색하기
def dfs(v): # v : 현재 노드
    result = 0 

    # 노드들을 탐색하며 더해준다.
    for i in tree[v]:
        result += dfs(i)

    # 노드의 타입이 늑대라면 빼준다.
    if node[v][0] == 'W':
        result -= node[v][1]
        if result < 0:
            result = 0
    # 노드의 타입이 양이라면 더해준다.
    else:
        result += node[v][1]
    return result

print(dfs(1))