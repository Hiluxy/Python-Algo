#틀림, 9/15 시간초과,,

def getMaximumRemovals(order, source, target):
    cnt=0
    s_index=[i for i in range(len(source))] #source인덱스
    if source==target:
        return 0
    else:
        for num in order:
            #해당 위치 빼기
            s_index.remove(num-1)
            #시퀀스 맞는지 확인
            if isTarget(source,target,s_index):
                cnt+=1
            else:
                break
        return cnt



def isTarget(word,target,s_index):
    index=0
    for i in s_index:
        if word[i] in target:
            if word[i] ==target[index]: #마지막 인덱스 아니면
                index+=1
                continue
            else: #j=마지막 인덱스까지 같음
                return True
    return False
                



print(getMaximumRemovals([1,4,2,3,5],"hkbdi","kd")) #1
print(getMaximumRemovals([7,1,2,5,4,3,6],"abbabaa","bb")) #3