r,c,time=6,7,3
input=[  ['.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', 'O', '.', '.', '.'],
  ['.', '.', '.', '.', '.', 'O', '.'],
  ['.', '.', '.', '.', '.', '.', '.'],
  ['O', 'O', '.', '.', '.', '.', '.'],
  ['O', 'O', '.', '.', '.', '.', '.']
]
graph=[[-1] * c for _ in range(r)]#폭탄시간저장 2차원그래프, 빈 공간:-1
empty=set() #빈 위치 저장


def printGraph(graph):
    for i in range(len(graph)):
        print(graph[i])  
    print()

#초기 그래프 갱신
for i in range(r):
    for j in range(c):
        if input[i][j]=='O':
            graph[i][j]=3
        else:
            graph[i][j]=-1

printGraph(graph)

while time>=0:
     
    #폭탄시간 -1 갱신
    for i in range(r):
        for j in range(c):
            graph[i][j]-=1
            #폭탄 터지면 터진위치+사방 set저장
            if graph[i][j]==0:
                empty.add((i,j))
                empty.add((i+1,j))
                empty.add((i-1,j))
                empty.add((i,j+1))
                empty.add((i,j-1))
                

    #폭탄 터진 위치를 -1으로 갱신해줌 
    for x,y in empty:
        if 0<=x<r and 0<=y<c:
            graph[x][y]=-1

    empty=set() #초기화(남은 범위 아닌 위치들)

    #봄버맨: 2초마다 설치
    if time%2==0:
        #빈 공간에 설치
        for i in range(r):
            for j in range(c):
                if graph[i][j]<=-1:
                    graph[i][j]=3
            
    time-=1
    printGraph(graph)
    

 

#출력
for i in range(r):
    for j in range(c):
        if graph[i][j]==-1:
            print(".")
        else:
            print("O")
    print()