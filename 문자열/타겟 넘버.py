from itertools import product


def solution(numbers, target):
    pm=[(x,-x) for x in numbers]
    nums=list(map(sum,product(*pm)))
    answer=nums.count(target)
    return answer

n1=[1, 1, 1, 1, 1]
t1=3
print(solution(n1,t1))