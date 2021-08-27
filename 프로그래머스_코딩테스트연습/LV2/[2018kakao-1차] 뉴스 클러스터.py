def strMaker(STR):
    word = STR.upper()
    arr = []

    for i in range(len(word) - 1):
        if 65 <= ord(word[i]) <= 90 and 65 <= ord(word[i + 1]) <= 90:
            tmp = ""
            tmp += word[i] + word[i + 1]
            arr.append(tmp)
    return arr


def checkPLUS(str1, str2):
    dic1 = {}
    dic2 = {}
    # print(str1,str2)
    for i in str1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1
    for i in str2:
        if i in dic2:
            dic2[i] += 1
        else:
            dic2[i] = 1
    sumcnt = 0
    for i in dic1:
        if i not in dic2:
            continue
        else:
            sumcnt += min(dic1[i], dic2[i])
    pluscnt = 0
    for i in dic2:
        if i in dic1:
            MAX = max(dic1[i], dic2[i])
            dic1[i] = MAX
        else:
            dic1[i] = dic2[i]
    for i in dic1:
        pluscnt += dic1[i]
    return sumcnt, pluscnt


def solution(str1, str2):
    str1 = strMaker(str1)
    str2 = strMaker(str2)
    if len(str1) == 0 and len(str2) == 0:
        return 65536
    sumcnt, pluscnt = checkPLUS(str1, str2)
    answer = sumcnt * 65536
    answer = answer // pluscnt

    return answer