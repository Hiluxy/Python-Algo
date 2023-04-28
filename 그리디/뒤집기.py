s=input()

cnt0=0 #모두 0일때 횟수
cnt1=0 #모두 1일때 횟수

if s[0]=='0':
    cnt1+=1
else:
    cnt0+=1

for i in range(len(s)-1):
    #전꺼랑 다음꺼랑 다르면
    if s[i]!=s[i+1]: 
        if s[i+1]=='1': #다음께 1 (0이 목표면 뒤집어야함)
            cnt0+=1
        else:
            cnt1+=1 

print(min(cnt0,cnt1))
  