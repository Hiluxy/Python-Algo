#N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

n,m=map(int,input().split())
arr=list(map(int,input().split()))
left=0
right=1
cnt=0
sum=arr[0]

while True:
    if(sum<m):
        if right<n:
            sum+=arr[right]
        else:
            break
    #m에 도달하면
    elif(sum==m):
        left+=1
        right=left+1
        sum=0
        cnt+=1
    #m에 도달하지 못하고 값만 커지면 -> 실패
    else:
        left+=1
        right=left+1
        sum=0
print(cnt)        
