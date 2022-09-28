import heapq
n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])
    print(q)

q.sort()
print('sort',q)

room = []
heapq.heappush(room, q[0][1])
print('room',room)

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])

print(len(room))



# import heapq

# n=int(input())
# arr=[]
# for _ in range(n):
#     a,b,c=map(int,input().split())
#     heapq.heappush(arr,(b,c))


# brr=[] #사용한 튜플은 여기 담기
# cnt=0

# for i in range(len(arr)):
#     if arr[i] not in brr:
#         end=arr[i][1] #기준점 끝시간
#         brr.append(arr[i])

#         for j in range(i,len(arr)):
#             if end<=arr[j][0] and arr[j] not in brr: #끝시간과 앞시간 비교
#                 brr.append(arr[j])
#         cnt+=1


# print(cnt)
