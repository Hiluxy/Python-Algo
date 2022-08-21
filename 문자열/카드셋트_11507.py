

str=input()

def SetCard(str):
  m=['P','K','H','T']
  ans=[13,13,13,13]

  total_length, split_length  = len(str), 3
  card_list=[ str[i:i+split_length] for i in range(0, total_length , split_length) ]

  for i in range(0,len(card_list)):
    for j in range(len(m)):
      if card_list[i][0]==m[j]:
        ans[j]-=1
    for j in range(i+1,len(card_list)):
      if card_list[i]==card_list[j]:
        return 'GRESKA'
  return ans

ans= SetCard(str)
if ans!='GRESKA':
  for i in ans:
    print(i,end=" ")
else:
  print(ans)

