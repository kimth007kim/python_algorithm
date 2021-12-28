from itertools import combinations


def check(colLst, row, relation):
    tmp = [tuple(item[idx] for idx in colLst) for item in relation]
    if len(set(tmp)) != row:
        return False
    else:
        return True


def solution(relation):
    column = len(relation[0])
    row = len(relation)
    colLst = range(column)
    arr = []

    for i in range(1, column + 1):
        comb = combinations(colLst, i)
        for n1 in list(comb):
            if check(n1, row, relation):
                arr.append(set(n1))

    for i in arr[:]:
        for j in arr[:]:
            if i == (i & j):
                if i != j:
                    arr.remove(j)

    return len(arr)