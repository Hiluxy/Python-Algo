def solution(info, query):
  info_l=[] #[["java","backend","junior","pizza","150"],[, , ,]]
  query_l=[]#[['java', 'backend', 'junior', 'pizza', '100'],[],[]]
  iscore=[]
  qscore=[]
  answer = []

  for i in info:
    info_l.append(list(i.split()))
  for i in query:
    i=i.replace(" and "," ")
    query_l.append(list(i.split()))

  for i in range(len(info_l)):
    num=0
    for j in range(4):
      if info_l[i][j]!=query_l[i][j]:
        break
      if int(info_l[i][5])>int(query_l[i][5])


  return query_l


info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))