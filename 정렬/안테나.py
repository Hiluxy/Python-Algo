
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
#중간값
print(arr[(n-1)//2])