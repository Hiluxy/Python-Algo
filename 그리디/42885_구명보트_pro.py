#https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()

    small_i=0
    j=len(people)-1
    cnt=0
    while i<=j:
      if people[i]+people[j]<=limit:
        i+=1
        j-=1
      else:
        j-=1
        cnt+=1
    return answer
