def solution(n, stages):
    answer=[]
    length=len(stages)

    for i in range(1,n+1):
        #해당 스테이지에 있는 사람
        count=stages.count(i)

        #실패율 
        if length==0:
            fail=0
        else:
            fail=count/length
        
        #(스테이지번호,실패율)삽입
        answer.append((i,fail))
        length-=count
    
    #실패율기준 내림차순
    answer.sort(key=lambda x:-x[1])

    #스테이지 번호 반환
    answer=[i[0] for i in answer]
    return answer
 
if __name__ == "__main__":
    print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))