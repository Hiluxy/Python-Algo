from itertools import permutations

def solution(numbers):
  nums=list(numbers)
  p=[]
  for i in range (1,len(nums)+1):
    p.append(list(permutations(nums,i))




print(solution("17"))