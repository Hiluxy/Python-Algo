#한줄씩 입력받기
#1. 
n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]
# 2
# 50 30
# 20 40
# [[50, 30], [20, 40]]


#2.
n=int(input())
g=[]
for i in range(n):
    g.append(list(map(int,input())))
