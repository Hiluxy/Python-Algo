# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    num_list=list(number)
    sort_list=sorted(num_list)
    del_list=[]
    for i in range(k):
        del_list.append(sort_list[i])
    for d in del_list:
        num_list.remove(d)
    answer = num_list.join()
    return answer