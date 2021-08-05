def isNumber(s):
    if s == "0" or s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8" or s == "9":
        return True
    return False


def divider(s):
    cnt = 0
    head = ""
    NUMBER = ""
    TAIL = ""
    end = len(s) - 1
    for i in range(len(s)):
        if isNumber(s[i]) and cnt == 0:
            cnt += 1
            head = s[:i]
            start = i
            continue
        if cnt == 1:
            if not isNumber(s[i]):
                end = i
                cnt = 2
                NUMBER = s[start:end]
                return head.upper(), int(NUMBER), s[end:]

    return head.upper(), int(s[start:len(s)]), ""


def solution(files):
    cnt = 0
    answer = []
    for s in files:
        head, number, tail = divider(s)
        # print(head,number,tail)
        cnt += 1
        answer.append((head, number, cnt, s))
        answer.sort(key=lambda x: (x[0], x[1], x[2]))

    result = []
    for head, number, tail, word in answer:
        result.append(word)
    return result