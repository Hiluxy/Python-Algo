from collections import deque

def solution(board, r, c):


    answer = 0
    return answer

def bfs(r,c,):
    que=deque()
    que.append((r,c))
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    visited = [[False for _ in range(4)] for _ in range(4)]
    visited[r][c] = True
    card=0
    while que:
        x,y=que.popleft()
        #4방향
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 안에 있음 & 카드 만남
            if 0<=nx<4 and 0<=ny<4 and board[nx][ny]!=0:
                #원래 카드랑 비교
                if card==board[nx][ny]:


            




if __name__ == "__main__":
    board=[[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
    r=[1,0]
    c=[0,1]
    #14,16
    for a,b,c in zip(board,r,c):
        print(solution(a,b,c))