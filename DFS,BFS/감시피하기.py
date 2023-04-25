from itertools import combinations


n=int(input())
graph=[] #그래프 정보
teacher_idx=[] #선생 위치(x,y)
empty_idx=[] #빈공간 위치(x,y)


for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        #선생, 빈 공간 위치 저장
        if graph[i][j]=='T':
            teacher_idx.append((i,j))
        if graph[i][j]=='X':
            empty_idx.append((i,j))

def teacherWatch(x,y,direction):
    #←왼
    if direction==0:
        while y>=0:
            if graph[x][y]=='S': #학생발견
                return True
            if graph[x][y]=='O': #장애물 발견->더 탐색 안함
                return False
            y-=1
    #오
    if direction==1:
        while y<n:
            if graph[x][y]=='S': #학생발견
                return True
            if graph[x][y]=='O': #장애물 발견->더 탐색 안함
                return False
            y+=1
    
    #위
    if direction==2:
        while x>=0:
            if graph[x][y]=='S': #학생발견
                return True
            if graph[x][y]=='O': #장애물 발견->더 탐색 안함
                return False
            x-=1
    #아래
    if direction ==3:
        while x<n:
            if graph[x][y]=='S': #학생발견
                return True
            if graph[x][y]=='O': #장애물 발견->더 탐색 안함
                return False
            x+=1
    return False

#장애물 설치 이후, 학생이 감지되는지 확인
def process():
    #모든 선생 위치
    for x,y in teacher_idx:
        #선생1의 4방향 확인 ->학생 하나라도 걸리면 true
        for i in range(4):
            if teacherWatch(x,y,i):
                return True
    return False


flag=False #장애물3개로 학생 다 숨기기 가능?
#빈공간 위치에서 장애물세울 3개 조합
for wall_idx in combinations(empty_idx,3):
    #장애물 설치
    for x,y in wall_idx:
        graph[x][y]='O'
    #프로세스 돌려보기
    if process():#실패, 장애물 회수하고 다시
        for x,y in wall_idx:
            graph[x][y]='X'
        continue
    if not process():#성공
        flag=True
        break

if flag:
    print('YES')
else:
    print('NO')

    
            