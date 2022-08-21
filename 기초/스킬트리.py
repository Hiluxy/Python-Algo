def solution(skill, skill_trees):
    answer = 0
    s = list(skill)
    visited = True
    d=0
    
    for a in skill_trees:
        visited = True
        for b in a:
            if b in s:
                c = s.index(b)
                if d == c:
                    d += 1
                else:
                    visited = False
                    print("실패" + b)
                    break
        if visited == True:
            answer += 1
            print("성공")
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))