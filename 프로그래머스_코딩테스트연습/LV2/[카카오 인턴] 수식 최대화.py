from itertools import permutations


def calc(a1, a2, op):
    if op == "+":
        return a1 + a2
    elif op == "-":
        return a1 - a2
    else:
        return a1 * a2


def remover(num, op, oper):
    cnt = 0
    if oper in op:
        for i in op[:]:
            if i == oper:
                t = num.pop(cnt + 1)
                num[cnt] = calc(num[cnt], t, i)
                op.pop(cnt)
                return
            else:
                cnt += 1


def solution(expression):
    # 숫자 배열 생성 완료
    sik = expression.replace("+", " ").replace("-", " ").replace("*", " ")
    numbers = list(map(int, sik.split()))

    # 순열로 식 생성 완료
    comb = list(permutations(["+", "*", "-"], 3))

    # 연산자 확인
    opers = []
    for i in expression:
        if i == "+" or i == "-" or i == "*":
            opers.append(i)

    answer = []
    for a, b, c in comb:
        num = numbers[:]
        op = opers[:]

        while len(num) != 1:
            if a in op:
                remover(num, op, a)
            elif a not in op and b in op:
                remover(num, op, b)
            elif a not in op and b not in op and c in op:
                remover(num, op, c)
            # break
        answer.append(num[0])
    MAX = -1e9
    for i in answer:
        if i < 0:
            MAX = max(-i, MAX)
        else:
            MAX = max(i, MAX)
    return MAX