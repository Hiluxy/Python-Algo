# https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3
import math

def solution(n, k):

  #1.진수 바꾸기
  knum=''
  while n>0:
    n,mod=divmod(n,k)
    knum+=str(mod)
  knum=knum[::-1]
  
  #2.슬라이싱
  plist=knum.split('0')

  #3.소수확인
  cnt=0
  for p in plist:
    re="YES"
    if p=='' or p=='1':
      continue
    for i in range(2,int(math.sqrt(int(p))) + 1):
      if int(p)%i==0:
        re="NO"
        break
    if re=="YES":
      cnt+=1
  
  return cnt

print(solution(110011,10))