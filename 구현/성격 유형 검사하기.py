# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	[7, 1, 3]	"RCJA"

def solution(survey, choices):
  dic={'R':0, 'T':0, 'C':0, 'F':0,'J':0,'M':0,'A':0,'N':0 }
  score=[0,3,2,1,0,1,2,3]
  for i in range(len(survey)):
    c_idx=choices[i]
    if choices[i]<4:
      dic[survey[i][0]]+=score[c_idx]
    else:
      dic[survey[i][1]]+=score[c_idx]

  print(dic)
  answer = ''
  if dic['R']<dic['T']:
    answer+='T'
  else:
    answer+='R'
  
  if dic['C']<dic['F']:
    answer+='F'
  else:
    answer+='C'
  
  if dic['J']<dic['M']:
    answer+='M'
  else:
    answer+='J'
  
  if dic['A']<dic['N']:
    answer+='N'
  else:
    answer+='A'
  
  return answer

s1,c1=["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]
s2,c2=["TR", "RT", "TR"],[7, 1, 3]

print(solution(s1,c1))
print(solution(s2,c2))