from collections import deque
import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
       return -1
    
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1)) #(음식다먹시간, 음식넘버)를 넣는다. 음식다먹시간 기준으로 정렬

    sum_passTime=0 #이전음식먹는데 썼던 시간
    preTime=0 #바로직전 다먹시간
    left_num=len(food_times) #남은음식 수

    #음식다먹시간이 가장 작은 음식부터 먹었다고 가정(나머지도 회전판돌며 그 다먹시간만큼 먹었겠지)
    #큐에서 하나씩 꺼내서 다 먹는다. 단 k를 넘기면 안된다
    while sum_passTime + (q[0][0]-preTime)*left_num<=k:
        nowTime=heapq.heappop(q)[0] 
        sum_passTime+=(nowTime-preTime)*left_num
        left_num-=1 #그 음식은 다 먹었다. 
        preTime=nowTime

    remain_foods =sorted(q, key=lambda x:x[1]) #큐에 남아있는 음식들은 덜 먹은 음식. 넘버순 정렬
    return remain_foods[(k-sum_passTime)%left_num][1]


#시간초과
# def solution(food_times, k):
#     if sum(food_times)<=k:
#         return -1
#     time=0 #현재시간
#     q=deque()
#     for i in range(len(food_times)):
#         q.append((i+1,food_times[i],0)) #(음식번호,다먹는데 걸리는 시간,먹은시간) 삽입
    
#     while time<k:
#         num,ft,eat_time=q.popleft()
#         #음식을 먹는다
#         eat_time+=1
#         time+=1
#         if ft==eat_time: #그 음식 다먹으면
#             continue
#         else: #다 못먹음
#             q.append((num,ft,eat_time)) #다시 큐에 삽입
    
#     #k초때 음식번호
#     answer=q.popleft()[0]

#     return answer