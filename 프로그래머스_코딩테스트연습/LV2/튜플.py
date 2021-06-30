def solution(s):
    answer = []
    a = list(map(str, s.split("}")))
    for i in range(len(a)):
        word = a[i][2:]
        if word != '':
            tmp = list(map(int, word.split(",")))
            answer.append(tmp)

    # print(answer)
    answer.sort(key=len)
    # print(answer)
    calc = []
    for i in range(len(answer)):
        n = answer.pop(0)
        for j in range(len(n)):
            if n[j] not in calc:
                calc.append(n[j])
        # print(n)
    return calc