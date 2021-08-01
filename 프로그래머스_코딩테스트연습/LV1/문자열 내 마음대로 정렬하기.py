def solution(strings, n):
    tmp = []
    for i in strings:
        tmp.append((i[n], i))

    a = sorted(tmp, key=lambda x: (x[0], x[1]))
    answer = []
    for i in a:
        answer.append(i[1])
    return answer