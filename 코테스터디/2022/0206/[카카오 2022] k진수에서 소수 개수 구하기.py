import math


def prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def convert(n, k):
    tmp = "0123456789"
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]


def solution(n, k):
    number = convert(n, k)
    cand = []
    tmp = ""
    start = 0
    for i, j in enumerate(number):
        if j == "0":
            if tmp != "":
                end = i
                cand.append([tmp, start, end - 1])
                tmp = ""
            else:
                continue
        else:
            if tmp == "":
                start = i
            tmp += j
        if i == len(number) - 1 and tmp != "":
            cand.append([tmp, start, i])
    answer = 0
    for num, start, end in cand:
        if prime_number(int(num)):
            # print("맞음",num,start,end)
            if start == 0 and end == len(number) - 1:
                # print("P처럼 소수 양쪽에 아무것도 없는 경우")
                answer += 1
            elif start - 1 >= 0 and end + 1 <= len(number) - 1 and number[end + 1] == "0" and number[start - 1] == "0":
                # print("0P0처럼 소수 양쪽에 0이 있는 경우")
                answer += 1


            elif start == 0 and end + 1 <= len(number) - 1 and number[end + 1] == "0":
                # print("P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우")
                answer += 1
            elif end == len(number) - 1 and start - 1 >= 0 and number[start - 1] == "0":
                # print("0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우")
                answer += 1

    return answer