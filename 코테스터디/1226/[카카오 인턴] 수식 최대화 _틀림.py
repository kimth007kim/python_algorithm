from itertools import permutations


def calc(p, number, oper):
    total = 0
    for i in p:
        while i in oper:
            for k, v in enumerate(oper):
                if v == i:

                    if i == "+":
                        tmp = number[k + 1] + number[k]
                    elif i == "-":
                        tmp = number[k] - number[k + 1]
                    else:
                        tmp = number[k + 1] * number[k]

                    number[k] = tmp
                    del number[k + 1]
                    del oper[k]
                    # print(i,number,oper)
    result = number[0]
    # print(result)
    if result < 0:
        result = -result
    return result


def solution(expression):
    giho = []
    if "+" in expression:
        giho.append("+")
    if "-" in expression:
        giho.append("-")
    if "*" in expression:
        giho.append("*")

    perm = list(permutations(giho, len(giho)))
    oper = []
    number = []
    answer = []
    start = 0

    # print(giho)
    for k, v in enumerate(expression):
        if v in giho:
            oper.append(v)
            tmp = (expression[start:k])
            start = k + 1
            number.append(int(tmp))

    number.append(int(expression[start:]))
    for p in perm:
        answer.append(calc(p, number[:], oper[:]))

    return max(answer)