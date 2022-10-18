n,m=map(int,input().split())
arr=list(map(int,input().split()))

# #반례
# m=6
# arr=[10,15]

def b(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        sum=0

        #sum을 구한다
        for i in arr: #[20, 15, 10, 17]
            if i>mid:
                sum+=i-mid
        
        if sum==target:
            return mid

        elif sum<target: #합이 부족하다
            end=mid-1

        elif sum>target: #합이 더 많다
            start=mid+1
            result=mid
    return result
            
print(b(arr,m,0,max(arr)))