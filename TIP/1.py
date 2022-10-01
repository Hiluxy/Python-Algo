from ast import Num
from tkinter import N
from typing import List
dic={} #{배열번호: [원소개수,배열사이즈]}

def solution(queries: List[List[int]]) -> int:
    cnt=0
    for s in queries:
        #없으면 해당 번호 배열 만들기, 처음은 걍 추가
        if s[0] not in dic:
            dic[s[0]]=[s[1],Size(s[1])]
        
        else:
            #원래개수+추가개수 <= 원래사이즈면 원소추가,사이즈 그대로
            if dic[s[0]][0]+s[1]<=dic[s[0]][1]:
                dic[s[0]][0]+=+s[1]
            #원래개수+추가개수 > 원래사이즈면 복사개수 저장, 원소추가,사이즈 늘리기
            else:
                cnt+=dic[s[0]][0]
                dic[s[0]][0]+=+s[1]
                dic[s[0]][1]=Size(dic[s[0]][0])
    return cnt

#a보다 최소로 큰 2의거듭제곱
def Size(a):
    n=1
    while a>n:
        n*=2
    return n

s=solution([[2,10],[7,1],[2,5],[2,9],[7,32]])
print(s)
