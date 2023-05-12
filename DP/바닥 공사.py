n=int(input())
d=[0]*(n+1)
d[1]=1
d[2]=3
for i in range(3,n+1):
    first_case=d[i-1]
    second_case=d[i-2]*2
    d[i]=first_case+second_case
print(d[n])