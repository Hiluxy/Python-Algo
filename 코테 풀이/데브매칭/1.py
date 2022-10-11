import re

def solution(registered_list, new_id):
    while new_id in registered_list:
        S = re.sub(r'[^a-z]', '', new_id)
        N = re.sub(r'[^0-9]', '', new_id)
        if N=='':
            N='0'
        new_N=str(int(N)+1)
        new_id=S+new_N
        
    return new_id
    
#print(solution(['abc','abc123','bc123'],'abc'))
print(solution(['cow','cow1','cow9'],'cow9'))




def solution(registered_list, new_id):
    num="0123456789"
    while new_id in registered_list:#존재유무시 시간복잡도 O(n), 딕셔너리로 만들어야 시간초과 안뜸~~#registered_list 딕셔너리 만들기
        S_list=[]
        for i in new_id:
            if i in num :
                break
            else:
                S_list.append(i)

        #S_list=[a,b,c]
        if len(S_list)==len(new_id):
            N='0'
        else:
            N=new_id[len(S_list):] #N="123"
        
        S=''.join(S_list)
        new_N=str(int(N)+1)
        new_id=S+new_N
        
    return new_id
'''
    테스트 1
입력값 〉
["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"
기댓값 〉
"ace15"
실행 결과 〉
테스트를 통과하였습니다.
테스트 2
입력값 〉
["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"
기댓값 〉
"cow10"
실행 결과 〉
테스트를 통과하였습니다.
테스트 3
입력값 〉
["bird99", "bird98", "bird101", "gotoxy"], "bird98"
기댓값 〉
"bird100"
실행 결과 〉
테스트를 통과하였습니다.
테스트 4
입력값 〉
["apple1", "orange", "banana3"], "apple"
기댓값 〉
"apple"
실행 결과 〉
테스트를 통과하였습니다.
'''