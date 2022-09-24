def solution(today, terms, privacies):
    answer=[]
    #약정 정의
    dic={}
    for t in terms:
        a,b=map(str,t.split())
        dic[a]=b
    
    #오늘날짜
    ty,tm,td=map(int,today.split('.'))

    idx=0
    for p in privacies:
        idx+=1
        term=int(dic[p[-1]])
        p = p[:-1]

        y,m,d=map(int,p.split('.'))
        m+=term
        while m>12:
            y+=1
            m-=12
            if m<=12:
                break

        if ty>y:
            answer.append(idx)
        elif ty==y and tm>m:
            answer.append(idx)
        elif ty==y and tm==m and td>=d:
            answer.append(idx)
        
    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))