#a는 문열고 b는 문 닫음. 냉장고문이 열려있는 총 시간은?
#입력: a가 여는 시점, b가 닫는 시점

def solution(openA,closeB):

  i=0
  j=0
  ans=0
  while True:
    if openA[i]<closeB[j]:
      ans+=closeB[j]-openA[i]
      j+=1
      while True:
        i+=1
        if openA[i]>closeB[j-1]:
          break

    else:
      j+=1
    
    # i나 j가 마지막 인덱스면 빠져나옴
    if i==len(openA)-1 or j==len(closeB)-1: 
      break
    print(i,j,ans)
  
  return ans



a1=[3,5,7]
b1=[4,10,12]
#6

a2=[4,7,9,16]
b2=[2,5,12,14,20]
#10

print(solution(a1,b1))
print(solution(a2,b2))
