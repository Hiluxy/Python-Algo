from collections import deque


def solution(n, computers):
    que=deque()
    que.append((computers[0])) #시작부분 담기
    
    while que:
        



if __name__ == "__main__":
    #11,-1
    board=[[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
    for b in board:
        print(solution(b))