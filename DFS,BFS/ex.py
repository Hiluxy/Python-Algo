from cgi import print_arguments


def solution(survey, choices):
    answer = ''
    sum = {"R": 0, "T": 0, "C": 0, "F":0, "J":0, "M":0, "A":0, "N":0}

    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]

        if choices[i] == 1:
            sum[a] += 3
        elif choices[i] == 2:
            sum[a] += 2
        elif choices[i] == 3:
            sum[a] += 1
        elif choices[i] == 5:
            sum[b] += 1
        elif choices[i] == 6:
            sum[b] += 2
        elif choices[i] == 7:
            sum[b] += 3

    if (sum["R"] > sum["T"]):
        answer += "R"
    else:
        answer += "T"

    if (sum["C"] > sum["F"]):
        answer += "C"
    else:
        answer += "F"

    if (sum["J"] > sum["M"]):
        answer += "C"
    else:
        answer += "J"

    if (sum["A"] > sum["N"]):
        answer += "A"
    else:
        answer += "N"


    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))