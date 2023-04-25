n=int(input())
students=[]
for _ in range(n):
    students.append(input().split())
#[['Junkyu', '50', '60', '100'], ...[이름,국,영,수 ] ]
#정렬기준: 국(내림),영(오름),수(내림),이름(사전순) 

students.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for student in students:
    print(student[0])