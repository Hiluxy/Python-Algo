s=input()
t=input()

def bfs(word):
    global t
    #print(word)
    if word==t:
        return 1
    if len(word)>len(t):
        return 0
    #첫 번째 경우 두 번째 경우 호출
    #print(one(word))
    #print(two(word))
    if bfs(one(word))==t or bfs(two(word))==t:
        return 1
    else: 
        bfs(one(word))
        bfs(two(word))


def one(word):
    return word+'A'

def two(word):
    w_list = list(word)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
    w_list.reverse() 
    word=''.join(w_list)
    return word+'B'

answer=bfs(s)
print(answer)
