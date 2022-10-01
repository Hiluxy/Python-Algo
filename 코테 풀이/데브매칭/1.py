import re

def solution(registered_list, new_id):
    while new_id in registered_list:
        S_list=[]
        #숫자문자열 추출 
        N = re.sub(r'[^0-9]', '', new_id)
        #S_list=[a,b,c]
        if len(S_list)==len(new_id):
            N='0'
        else:
            N=new_id[len(S_list):] #N="123"
        
        S=''.join(S_list)
        new_N=str(int(N)+1)
        new_id=S+new_N
        
    return new_id
    
#print(solution(['abc','abc123','bc123'],'abc'))
print(solution(['cow','cow1','cow9'],'cow9'))
'''
def solution(registered_list, new_id):
    num="0123456789"
    while new_id in registered_list:
        S_list=[]
        #아이디 흝기
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