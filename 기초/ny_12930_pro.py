# https://school.programmers.co.kr/learn/courses/30/lessons/12930?language=python3
def solution(s):
    word_l=list(map(str,s.split()))
    for word in word_l:
      for i in range(len(word)):
        if i%2==0:
          word[i].lower()
        if i%2==1:
          word[i].upper()    
    answer = ''.join(word_l)
    return answer

solution("try hello world"	)