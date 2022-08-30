#a는 문열고 b는 문 닫음. 냉장고문이 열려있는 총 시간은?
#입력: a가 여는 시점, b가 닫는 시점
#항상 b가 마지막으로 닫음. a랑 b 시점 겹치지 않음. 

def solution(openA,closeB):

  i=0
  j=0
  ans=0
  while True:
    if openA[i]<closeB[j]:
      ans+=closeB[j]-openA[i]
      while True:
        i+=1
        if i==len(openA)-1:
          break
        if openA[i]>closeB[j]:
          break

      #i가 마지막 인덱스이면서 closeB[j]보다 작음: 더 세어줄 필요가 없음. 
      if i==len(openA)-1 and openA[i]<closeB[j]:
        return ans

      while True:
        j+=1
        if openA[i]<closeB[j]:
          break

    else:
      j+=1
    
    # j가 마지막 인덱스면(항상 openA[i]<closeB[j]) 계산하고 빠져나옴
    if j==len(closeB)-1: 
      ans+=closeB[j]-openA[i]
      return ans



a1=[3,5,7]
b1=[4,10,12]
#6

a2=[4,7,9,16]
b2=[2,5,12,14,20]
#10

print(solution(a1,b1))
print(solution(a2,b2))
