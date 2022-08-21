#내 풀이
str=input()

sum=0
for s in str:
  if int(s) <=1 or sum<=1:
    sum+=int(s)
  else:
    sum*=int(s)

print(sum)