# 🔶교재: 이것이 코딩 테스트다 with 파이썬 - 나동빈
# Chapter 6 정렬
# 실전문제 3 성적이 낮은 순서로 학생 출력하기
# https://im-the-best-output.tistory.com/98

k=int(input())
arr=[]
for _ in range(k):
    arr.append(list(input().split()))
result = sorted(arr, key=lambda x:x[1])
for i in range(k):
    print(result[i][0],end=' ')

