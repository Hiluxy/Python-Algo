n=int(input())
g=[[] for _ in range(n+1)] #연결 노드 저장
sw_num=[[] for _ in range(n+1)] #[[] ['S',100]...]
visited=[False for _ in range(n+1)]
tail=[]

for i in range(2,n+1): #2번노드부터 n까지
    a,b,c=map(str,input().split())
    b=int(b)
    c=int(c)
    g[i].append(c)
    g[c].append(i)
    sw_num[i].append([a,b])

#sw_num=[[], [], [['S', 100]], [['S', 100]], [['W', 100]], [['S', 1000]], [['W', 1000]], [['S', 900]]]
#g=[[], [2, 3, 4], [1, 5, 6], [1], [1], [2], [2, 7], [6]]

def bfs(v):
    if visited[v]==True:
        tail.append(v)
    else:
        visited[v]=True
        for i in g[v]:#[2,3,4]
            if visited[i]==False:
                bfs(i)

bfs(1)
print(tail)