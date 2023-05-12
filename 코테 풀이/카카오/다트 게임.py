#옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.


def solution(dartResult):
    point=0
    bonus={"S":1,"D":2,"T":3}
    #opt={"*":2,"#":-1}
    num_arr=[]
    answer=0
    while point<len(dartResult):
          #숫자확인
          if dartResult[point:point+2]=="10": # 10인지 확인
                      num_arr.append(10)
                      point+=2
          else: 
            num=int(dartResult[point])
            num_arr.append(num)
            point+=1
                
            #보너스
            num=num_arr[-1:]
            num_arr[-1:]=num**bonus[dartResult[point]]
            point+=1

            #옵션
            if point <len(dartResult):
                if dartResult[point] =="*":
                 num[-1:]*=2
                 if len(num)!=1:
                      num[-2:]*2
                else:
                     num[-1:]*=(-1)
                 
                point+=1 
    
    answer=sum(num)
    return answer

if __name__ == "__main__":
	print(solution("1S2D*3T"))