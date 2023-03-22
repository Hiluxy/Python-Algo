#여행가가 (1,1)~(n,n) 정사각형 좌표에 있음. 공간 벗어나면 무시
#첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1<=N<=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1<=이동 횟수<=100)
# 출력
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력

# 입력 예시
# 5
# R R R U D D

# 출력 예시
# 3 4

spot=[1,1]
n=int(input())
steps=list(input().split())
dic={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}
for step in steps:
    n_row=spot[0]+dic[step][0]
    n_column=spot[1]+dic[step][1]
    if 1<=n_row<=n and 1<=n_column<=n:
        spot[0]=n_row
        spot[1]=n_column

print(spot[0],spot[1])
