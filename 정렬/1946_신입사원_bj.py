#https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline


def PassNum(rank_list):
  rank_list.sort()
  cnt=0
  max=rank_list[0][1]
  for me in rank_list:
    if me[1]<=max:
      max=me[1]
      cnt+=1
  return cnt

for tc in range(int(input())):
  a=int(input())
  rank_list=[]
  for _ in range(a):
    rank_list.append(list(map(int,input().split())))
  print(PassNum(rank_list))
