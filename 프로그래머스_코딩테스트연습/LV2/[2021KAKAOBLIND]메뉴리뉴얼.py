from itertools import combinations


def solution(orders, course):
    answer = []
    order = []

    data = [[] for _ in range(len(course))]
    MAXVALUE = [0] * len(course)
    # print(MAXVALUE)

    # order 안의 메뉴를 list화
    for i in orders:
        order.append(list(i))

    menu = {}

    for i in order:
        for j in course:
            if j > len(i):
                break
            comb = combinations(i, j)
            # print(list(comb))
            for k in list(comb):
                arr = list(k)
                arr.sort()
                word = "".join(arr)
                if word in menu:
                    menu[word] += 1
                else:
                    menu[word] = 1

    for i in menu:
        for j in range(len(course)):
            if len(i) == course[j]:
                if menu[i] > 1:
                    if MAXVALUE[j] < menu[i]:
                        MAXVALUE[j] = menu[i]
                    data[j].append((i, menu[i]))

    for i in range(len(data)):
        for name, val in data[i]:
            if val == MAXVALUE[i]:
                answer.append(name)
            # print(name,val)
        # print(data[i],MAXVALUE[i])
        # if data[i]==MAXVALUE[i]
    # for i in data:
    #     # mx
    #     print(i)
    # print(MAXVALUE)
    answer.sort()

    return answer