def solution(record):
    answer = []
    c=[]
    id={}
    for re in record:
      c.append(list(map(str,re.split())))
    #c=[['Enter', 'uid1234', 'Muzi'], ['Enter', 'uid4567', 'Prodo'], ['Leave', 'uid1234'], ['Enter', 'uid1234', 'Prodo'], ['Change', 'uid4567', 'Ryan']]

    #Enter,Change때 닉네임 갱신, id에 id:닉네임 저장.
    for re in c:
      if re[0]=='Enter':
        id[re[1]]=re[2]
        
      elif re[0]=='Change':
        id[re[1]]=re[2]
      
    for re in c:
      if re[0]=='Enter':
        answer.append(id[re[1]]+"님이 들어왔습니다.")
      elif re[0]=='Leave':
        answer.append(id[re[1]]+"님이 나갔습니다.")


    return answer


record=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
