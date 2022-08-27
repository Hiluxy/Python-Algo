from collections import deque
import math
from collections import deque

def solution(progresses, speeds):
  answer = []
  day=deque()
  for i in range(len(progresses)):
    day.append(math.ceil(((100-progresses[i])/speeds[i])))
  
  cnt=1
  max_day=day[0]
  for _ in range(len(progresses)-1):
    if max_day>day[1]:
      cnt+=1
    else:
      answer.append(cnt)
      cnt=1
      max_day=day[1]
    day.popleft()

  return answer



p=[95, 90, 99, 99, 80, 99]
s=[1, 1, 1, 1, 1, 1]	
print(solution(p,s))