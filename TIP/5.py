def solution(commands):
    answer = []
    table = [['O']*51] * 51
    for cword in commands:
        c=list(cword.split())#['UPDATE', '1', '1', 'menu']
        if c[0]=='UPDATE':
            if len(c)==4:
                table[int(c[1])][int(c[2])]=c[3]
            if len(c)==3:
                newlist=[(i,j) for i in range(51) for j in range(51) if table[i][j]==c[1]]
                for r,c in newlist:
                    table[int(r)][int(c)]=c[2]
        elif c[0]=='MERGE':
            r1,c1,r2,c2=int(c[1]),int(c[2]),int(c[3]),int(c[4])
            #둘 다 값이 있음
            if table[r1][c1]!='O' and table[r2][c2]!='O':
                #병합된 값은 table[r1][c1]
                table[r2][c2]=table[r1][c1]
            #한 쪽만 값이 있음
            elif table[r1][c1]!='O' and table[r2][c2]=='O':
                #table[r1][c1]값
                table[r2][c2]=table[r1][c1]
            elif table[r1][c1]=='O' and table[r2][c2]!='O':
                #table[r2][c2]값
                table[r1][c1]=table[r2][c2]
        elif c[0]=='UNMERGE':
            r,c=int(c[1]),int(c[2])
            #table[r][c]만 값 가지고 나머진 'O'
            temp=table[r][c]
            nlist=[(i,j) for i in range(51) for j in range(51) if table[i][j]==table[r][c]]
            for i,j in nlist:
                table[i][j]='O'
            table[r][c]=temp
        elif c[0]=='PRINT':
            ans=table[int(c[1])][int(c[2])]
            if ans=='O':
                ans='EMPTY'
            print(cword,ans)
            answer.append(ans) 
    return answer

q1=["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
q2=["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(q2))