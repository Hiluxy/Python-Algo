n=int(input())
star=["***","* *","***"]
cnt=0

def Star(star):
  g=[]
  for i in range(3*len(star)):
    if i//len(star)==1: #i번째블록을 행길이로 나눠 몫1인애 (공백이 있는 행만 걸러짐)
      g.append(star[i%len(star)]+" "*len(star)+star[i%len(star)])
    else: 
      g.append(star[i%len(star)]*3)
  return g

#입력은 3^cnt
while n>3:
  n/=3
  cnt+=1

for i in range(cnt):
  star=Star(star)

for i in star:
  print(i)