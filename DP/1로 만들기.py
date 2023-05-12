#1을 빼는 경우는 항상 있기때문에 맨 앞으로,d[i]=0방지
#for문 시작점 

x=int(input())
d=[0]*30001

for i in range(2,x+1):
    #1을 빼는 경우
    d[i]=d[i-1]+1

    #2로 나누어떨어지면
    if i%2==0:
        before_num=i//2
        d[i]=min(d[i],d[before_num]+1)
    #3으로 나누어떨어지면
    if i%3==0:
        before_num=i//3
        d[i]=min(d[i],d[before_num]+1)
    #5로 나누어떨어지면
    if i%5==0:
        before_num=i//5
        d[i]=min(d[i],d[before_num]+1)

print(d[0:x+1])