n=int(input())
arr=list(map(int, input().split()))
d=[0]*(n+1)
d[0]=arr[0]
d[1]=max(arr[0],arr[1])
for i in range(2,n):
    first_case=d[i-1]
    second_case=d[i-2]+arr[i]
    d[i]=max(first_case,second_case)
print(max(d))