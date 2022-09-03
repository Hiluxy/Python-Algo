n=int(input())
num=[[0]*3 for _ in range(n+1)]

num[1][0]=1  
num[1][1]=1 
num[1][2]=1 

for i in range(2,n+1):
  num[i][0]=(num[i-1][0]+num[i-1][1]+num[i-1][2])%9901
  num[i][1]=(num[i-1][0]+num[i-1][2])%9901
  num[i][2]=(num[i-1][0]+num[i-1][1])%9901

print(sum(num[n])%9901)