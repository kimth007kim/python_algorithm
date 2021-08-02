def reverse(s, n):
    left = s[:n]
    right = s[n:]
    tmp = right + left
    return tmp


def check(s):
    calc = []
    bigcnt = 0
    middlecnt = 0
    smallcnt = 0
    for i in s:
        if i == "{":
            calc.append("1")
        elif i == "}":
            calc.append("-1")
            if len(calc) < 2:
                return False
            if calc[-2] == "1":
                calc = calc[:-2]
        elif i == "[":
            calc.append("2")
        elif i == "]":
            calc.append("-2")
            if len(calc) < 2:
                return False
            if calc[-2] == "2":
                calc = calc[:-2]

        elif i == "(":
            calc.append("3")
        elif i == ")":
            calc.append("-3")
            if len(calc) < 2:
                return False
            if calc[-2] == "3":
                calc = calc[:-2]

    if len(calc) == 0:
        return True
    else:
        return False


def solution(s):
    tmp = []
    cnt = 0
    for i in range(len(s)):
        word = reverse(s, i)
        # print(word)
        if check(word):
            cnt += 1
    return cnt