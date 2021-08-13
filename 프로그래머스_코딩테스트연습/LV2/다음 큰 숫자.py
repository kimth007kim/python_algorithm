def checker(number):
    word = str(number)
    cnt = 0
    for i in word:
        if i == "1":
            cnt += 1
    return cnt


def binaryPlus(cnt, number):
    while True:
        a = int("1", 2)
        number = int(number, 2)
        number += a
        number = bin(number)[2:]
        if checker(number) == cnt:
            return number


def solution(n):
    answer = 0
    nNum = bin(n)[2:]
    cnt = checker(nNum)
    answer = binaryPlus(cnt, nNum)
    return int(str(answer), 2)