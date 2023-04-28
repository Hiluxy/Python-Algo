n,m=map(int,input().split())
arr=list(map(int,input().split()))

sum=0
start=0
end=max(arr)
result=0 #주의

while start<=end:
    sum=0
    mid=(start+end)//2 #mid는 항상 갱신해주기! 

    #sum구하기
    for a in arr:
        if a>mid:
            sum+=a-mid
    if sum==m:
        result=mid
        break
    elif sum<m: #자른게 목표보다 작으면
        end=mid-1 #end를 왼쪽으로
    else: #자른게 목표보다 크면
        start=mid+1 #start를 오른쪽으로 
        result=mid #기록해두기

print(result)