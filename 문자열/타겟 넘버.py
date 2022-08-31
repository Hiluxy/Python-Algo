from itertools import product


def solution(numbers, target):
    pm=[(x,-x) for x in numbers]
    # # for x in numbers:
    #     pm.append((x,-x))
    nums=list(map(sum,product(*pm)))  
    answer=nums.count(target)
    return answer

n1=[1, 1, 1, 1, 1]
t1=3
print(solution(n1,t1))