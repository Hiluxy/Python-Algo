from collections import deque
import math

def solution(progresses, speeds):
  answer = []
  day=deque()
  for i in range(len(progresses)):
    day.append(math.ceil(((100-progresses[i])/speeds[i])))
  
  cnt=1
  max_day=day[0]
  for _ in range(len(progresses)-1):
    if max_day>=day[1]:
      cnt+=1
    else:
      answer.append(cnt)
      cnt=1
      max_day=day[1]
    day.popleft()
  
  #마지막 인덱스 처리  
  if max_day>day[0]:
      answer.append(cnt)
  else:
      answer.append(1)
  
  

  return answer



p=[95, 90, 99, 99, 80, 99]
s=[1, 1, 1, 1, 1, 1]	
#[5,10,1,1,20,1]
p2=[93, 30, 55]
s2=[1, 30, 5]
print(solution(p2,s2))