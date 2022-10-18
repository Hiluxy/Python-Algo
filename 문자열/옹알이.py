#못품
#1 ≤ babbling의 길이 ≤ 10
# 1 ≤ babbling[i]의 길이 ≤ 30
#"aya", "ye", "woo", "ma"만 발음 가능 (주의: 연속 발음 불가)


def solution(babbling):
    baby=["aya", "ye", "woo", "ma"]
    for word in babbling:
        for b_word in baby:
            if word[0]==b_word[0]:
                for i in range(b_word):
                    if b_word[i]==word[i]:
                        continue
                    else: break
                #b_word만큼 지우기

    
    answer = 0
    return answer

if __name__ == "__main__":
    print(solution(["aya", "yee", "u", "maa"]))#1
    print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))#2