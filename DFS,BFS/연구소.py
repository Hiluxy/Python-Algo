n,m=map(int,input().split())
graph=[] #초기 맵
temp=[[0]*m for _ in range(n)] #벽 3개 설치 뒤의 맵

for _ in range(n):
    graph.append(list(map(int,input().split())))

#4 이동방향
dx=[-1,0,1,0]
dy=[0,1,0,-1]

result=0

#dfs로 각 바이러스가 사방에 퍼짐
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #바이러스가 퍼질 수 있는 경우: 범위 안에 있음 & 빈공간
        if nx>=0 and nx<n and ny >=0 and ny <m:
            if temp[nx][ny]==0:
                #바이러스 퍼짐
                temp[nx][ny]=2
                virus(nx,ny)


#안전 영역 크기 계산
def getScore():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score +=1
    return score

#dfs로 울타리 3개 설치, 안전영역 크기 계산 반복하며 max갱신
def installFence(cnt):
    global result
    #울타리 3개 설치완료 -> map으로 옮겨서 안전영역 계산
    if cnt ==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]==graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        
        result=max(result,getScore())
        return
    
    #빈공간 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j]=1
                cnt+=1
                installFence(cnt) #울타리3개까지설치했음 -> 들어가서 바이러스 퍼트려보고 안전영역 계산, 다시 나옴
                graph[i][j]=0 #백트래킹 
                cnt-=1

installFence(0)
print(result)