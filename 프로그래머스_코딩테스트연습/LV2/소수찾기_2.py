from itertools import permutations


def sosoo(number):
    for i in range(2, number):
        if number % i == 0:
            # print("sss ",i)
            return False
    return True


def solution(numbers):
    data = list(numbers)
    l = len(data)
    arr = []
    for i in range(1, l + 1):
        comb = permutations(data, i)
        for j in list(comb):
            a = list(j)
            if a[0] == "0":
                a.pop(0)
            if len(a) > 0:
                d = int("".join(a))
                if d not in arr and d != 1 and d != 0:
                    arr.append(d)

    cnt = 0
    # print(arr)
    for i in arr:
        if sosoo(i):
            cnt += 1

    return cnt