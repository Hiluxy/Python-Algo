# 8 × 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는
# 프로그램을 작성하라. 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는
# a 부터 h로 표현한다
# 입력 예시
# a1

# 출력 예시
# 2

spot=input()
row=int(spot[1])
column=int(ord(spot[0]))-int(ord('a'))+1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

cnt=0
for step in steps:
    n_row=row+step[0]
    n_column=column+step[1]
    #이동 가능하면 카운트
    if 8>=n_row>=1 and 8>=n_column>=1:
        cnt+=1
print(cnt)