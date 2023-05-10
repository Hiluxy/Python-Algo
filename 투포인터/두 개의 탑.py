import sys
input=sys.stdin.readline
n=int(input())
arr=[int(input()) for _ in range(n)]

total=sum(arr)

left=right=dist=result=0
i=0
while 1:
    if dist>result:
        dist-=arr[left]
        left+=1 
    if right==n:
        break
    else:
        dist+=arr[right]
        right+=1
    
    if dist==total//2:
        result=dist
        break
    #결과 갱신
    result=max(result, min(dist,total-dist))
    print(i,left,right)
    i+=1
print(result)