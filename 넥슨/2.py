#틀림, 9/15 시간초과,,

from collections import deque


def getMaximumRemovals(order, source, target):
    cnt=0
    if source==target:
        return 0
    s_list=list(source)
    else:
        for num in order:
            #해당 위치 빼기
            s_list.pop(num-1)
            s_list.insert(num,'-')
            #시퀀스 맞는지 확인
            if isTarget(source,target):
                cnt+=1
            else:
                break
        return cnt



def isTarget(word,target):
    j=0
    for i in s_index:
        if word[i]==target[j]:
            if j !=len(target)-1: #마지막 인덱스 아니면
                j+=1
            else: #j=마지막 인덱스까지 같음
                return True
    return False
                



print(getMaximumRemovals([1,4,2,3,5],"hkbdi","kd")) #1
print(getMaximumRemovals([7,1,2,5,4,3,6],"abbabaa","bb")) #3