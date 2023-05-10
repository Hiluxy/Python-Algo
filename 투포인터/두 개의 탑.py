n=int(input())
arr=[int(input()) for _ in range(n)]

start=0
result=0
for start in range(n):
    distance=0
    for point in range(start+1,n):
        distance+=arr[point]
        if distance<=sum(arr)-distance: 
            result=max(result,distance)
        else:
            continue

print(result)
        
        