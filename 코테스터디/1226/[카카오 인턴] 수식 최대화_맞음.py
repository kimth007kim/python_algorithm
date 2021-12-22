from itertools import permutations

def calc(perm, num, oper, dic):
    for op in perm:
        if op in dic:
            for i in range(dic[op]):  # 딕셔너리에 있는 값만큼 돌린다.
                for k, v in enumerate(oper):
                    if v == op:
                        print(oper[k])
                        print(num[k], num[k + 1])
                        del oper[k]
                        if op == "+":
                            num[k] += num[k + 1]
                        elif op == "-":
                            num[k] -= num[k + 1]
                        else:
                            num[k] *= num[k + 1]
                        del num[k + 1]
                        break
    total = num[0]
    if total < 0:
        total = -total
    return total


def solution(expression):
    answer = []
    tmp = expression.replace("+", " ").replace("*", " ").replace("-", " ")
    num = list(map(int, tmp.split()))
    oper = []
    dic = {}
    for i in expression:
        if i == "*" or i == "+" or i == "-":
            oper.append(i)
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
    comb = list(permutations(["+", "-", "*"], 3))
    for perm in comb:
        answer.append(calc(perm, num[:], oper[:], dic))

    return max(answer)