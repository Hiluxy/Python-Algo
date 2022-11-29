n,m =map(int,input().split())
g=[[0 for _ in range(m)]for _ in range(n)]
q=[]

for _ in range(int(input())):
    q.append(list(map(int,input().split())))

print(q)