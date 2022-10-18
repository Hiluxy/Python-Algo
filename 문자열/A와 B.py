s=list(input())
t=list(input())

while len(t)!=len(s):
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t=t[::-1]
if t==s:
    print(1)
else:
    print(0)
