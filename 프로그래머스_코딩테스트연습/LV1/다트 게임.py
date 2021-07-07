def divided(dartResult):
    tmp = ""
    word = []
    ccnt = 0
    ncnt = 0
    for i in range(len(dartResult)):
        if ord(dartResult[i]) == 68 or ord(dartResult[i]) == 83 or ord(dartResult[i]) == 84:
            ccnt += 1
        if 48 <= ord(dartResult[i]) <= 57:
            ncnt += 1
        if ncnt >= 1 and ccnt == 1 and 48 <= ord(dartResult[i]) <= 57 and i != 0:
            word.append(tmp)
            tmp = ""
            ncnt = 1
            ccnt = 0
        tmp += dartResult[i]
        if i == len(dartResult) - 1:
            word.append(tmp)
    return word


def calc(text):
    double = 0
    if ord(text[1]) == 48:
        score = 10
        text = text[2:]
    else:
        score = int(text[0])
        text = text[1:]
    for i in text:
        if i == "D":
            score = score ** 2
        if i == "T":
            score = score ** 3
        if i == "*":
            score *= 2
            double = 2
        if i == "#":
            score = -score
    return score, double


def solution(dartResult):
    answer = 0
    word = divided(dartResult)
    arr = []
    for i in word:
        score, double = calc(i)
        arr.append((score, double))
    isDouble = 0
    for i in range(2, -1, -1):
        score, double = arr[i]
        # print("------",score,double,"isDouble",isDouble)
        if isDouble == 2:
            answer += score * 2
            isDouble = 0
        else:
            answer += score
        if double == 2:
            isDouble = 2
    # print(arr)

    return answer