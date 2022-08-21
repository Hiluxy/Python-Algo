from collections import deque
def solution(nums, target):
    answer = 0
    que = deque()
    n = len(nums)
    que.append([nums[0],0])
    que.append([-1*nums[0],0])
    while que:
        temp, idx = que.popleft()
        idx += 1
        if idx < n:
            que.append([temp+nums[idx], idx])
            que.append([temp-nums[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer