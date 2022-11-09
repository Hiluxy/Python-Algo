import math
import sys
input = sys.stdin.readline

dec=[]
#에라토스테네스의 채
#소수 배열 dec 설정
def is_prime_num(n):
    global dec
    arr = [True] * (n + 1)
    arr[0] = False
    arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2

            while (i * j) <= n:
                arr[i*j] = False
                j += 1
    
    for i in range(n+1):
        if arr[i]==True:
            dec.append(i)

def solution(target):
    global dec
    is_prime_num(target) #target보다 작은 배열 생성
    
    left,right=0,1
    cnt=0
    for left in range(len(dec)):
        right=left+1
        while tmp<target and right<len(dec):
            tmp=sum(dec[left:right+1])
            right+=1
            if tmp==target:
                cnt+=1
                break
    
    return cnt

if __name__ == '__main__':
    target=int(input())
    print(solution(target))