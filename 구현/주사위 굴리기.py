n,m,x,y,k=map(int,input().split())
g=[list(map(int,input().split())) for _ in range(n)]
d=list(map(int,input().split()))

#위/앞부터(시계방향)/아래
dice=[0,0,0,0,0,0] 

dx=[0,0,0,-1,1] #direction은 1-4임에 유의
dy=[0,1,-1,0,0]

#현재위치 초기화
nx,ny=x,y

for direction in d:
  
  #범위 벗어나면 예외처리
  if nx+dx[direction]<0 or nx+dx[direction]>=n or ny+dy[direction]<0 or ny+dy[direction]>=m:
    continue

  #주사위 내용 바꿔주기 
  if direction==1:
    dice[0],dice[2],dice[4],dice[5]=dice[4],dice[0],dice[5],dice[2]
  elif direction==2:
    dice[0],dice[2],dice[4],dice[5]=dice[2],dice[5],dice[0],dice[4]
  elif direction==3:
    dice[0],dice[1],dice[3],dice[5]=dice[1],dice[5],dice[0],dice[3]
  elif direction==4:
    dice[0],dice[1],dice[3],dice[5]=dice[3],dice[0],dice[5],dice[1]

  #주사위 위치 바꿔주기
  nx+=dx[direction]
  ny+=dy[direction]

  #이동칸 수가 0
  if g[nx][ny]==0:
      g[nx][ny]=dice[5]
  else:
    dice[5]=g[nx][ny]
    g[nx][ny]=0

  print(dice[0])
  

