def solution(survey, choices):
    answer = ""
    count = dict()
    test = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
    for a, b in test:
        count[a] = 0
        count[b] = 0

    for i in range(len(survey)):
        A, B = survey[i][0], survey[i][1]
        point = choices[i]
        if point == 4:
            continue
        if point < 4:
            count[A] += 4 - point
        else:
            count[B] += point - 4

    for a, b in test:
        if count[a] >= count[b]:
            answer += a
        else:
            answer += b
    return answer