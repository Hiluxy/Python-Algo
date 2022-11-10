n,s=map(int,input().split())
arr=list(map(int,input().split()))
result=100000
left,right=0,1
for left in range(len(arr)):
    right=left+1
    tmp=arr[left]
    while(tmp<s and right<len(arr)):
        tmp+=arr[right]
        right+=1
    if tmp==s:
        result=min(result,right-left)
        continue
    if tmp>s:
        continue

print(result)


