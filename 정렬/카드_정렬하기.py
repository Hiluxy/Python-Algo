import heapq

heap=[]
n=int(input())

#힙에 초기 카드묶음 넣음
for _ in range(n):
    heapq.heappush(heap,int(input()))

#힙 안에 원소가 1개가 될때까지
result=0
while len(heap)!=1:
    sum=heapq.heappop(heap)+heapq.heappop(heap)
    result+=sum
    heapq.heappush(heap,sum)

print(heapq.heappop(heap))