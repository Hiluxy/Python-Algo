

def solution(info, query):
    info_l=[] 
    query_l=[]
    answer = []

    for i in info:
        info_l.append(list(i.split()))
    for i in query:
        i=i.replace(" and "," ")
        query_l.append(list(i.split()))

    for query in query_l:
        num=0
        for person in info_l:
            check=[]
            #조건 0~3까지 확인
            for i in range(4):
                if person[i]==query[i] or query[i]=='-':
                    check.append(1)
                else:
                    check.append(0)
            #조건4 확인
            if int(person[4])>=int(query[4]):
                    check.append(1)
            else:
                check.append(0)
            if check==[1,1,1,1,1]:
                num+=1
        answer.append(num)

    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))