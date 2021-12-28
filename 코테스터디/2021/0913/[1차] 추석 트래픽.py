def timeMaker(s):
    hr, mn, sec = s.split(":")
    sc, ms = sec.split(".")
    total = int(hr) * (60 * 60 * 1000) + int(mn) * (60 * 1000) + int(sc) * 1000 + int(ms)
    return total


def miliSecond(t):
    if len(t) == 2:
        thousand, last = int(t[0]), 0
    else:
        thousand, last = t[:-1].split(".")
        if len(last) == 1:
            last = int(last) * 100
        elif len(last) == 2:
            last = int(last) * 10
        else:
            last = int(last)
    result = int(thousand) * 1000 + last
    return result


def calcRecord(num, dic):
    tmp = []
    tmp += dic[num]
    for i in range(num, num + 1000):
        if i not in dic:
            continue
        else:
            if dic[i] == dic[num]:
                continue
            else:
                tmp += dic[i]

    tmp = list(set(tmp))
    return len(tmp)
    # print(len(list(set(tmp))))


def solution(lines):
    answer = 0
    dic = {}
    arr = []

    first = int(1e9)
    MIN = 0
    for i in range(len(lines)):
        tmp = []
        date, s, t = lines[i].split()
        remain = miliSecond(t)
        end = timeMaker(s)
        start = end - remain + 1
        if start < 0:
            start = 0
        if start > 86400000:
            start = 86400000
        if end > 86400000:
            end = 86400000

        first = min(first, start)
        arr.append([start, end])

    for i in range(len(arr)):
        start, end = arr[i]
        for j in range(start - first, end - first + 1000):
            # if j>86400000:
            #     break
            if j not in dic:
                dic[j] = [i + 1]
            else:
                dic[j].append(i + 1)

    # print(dic)
    for i in dic:
        answer = max(answer, len(dic[i]))

    # for i in dic:
    #     answer = max(answer,calcRecord(i,dic))
    # break

    return answer