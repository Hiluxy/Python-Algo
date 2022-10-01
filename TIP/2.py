from typing import List
from itertools import product

#['a', 'b', 'c', 'd', ... , 'x', 'y', 'z']
alpha=[chr(i) for i in range(97,123)]


def solution(k: int, dic: List[str], chat: str) -> str:
    #.을 대체할 수 있는 리스트
    dotlist=[]
    for _ in range(1,k+1):
        dotlist+=list(map("".join,(product(alpha,repeat=_)))) 
    
    chat_list=chat.split()
    for c in chat_list:
        #비속어 자체
        if c in dic:
            c='#'*len(c)
        #.이 들어갈경우
        elif '.' in c:
            new=[]
            while '.' in new:
            for i in range(len(c)):
                if c[i]=='.':
                    for dotc in dotlist:
                        c[i]=dotc
                        new.append(c)

