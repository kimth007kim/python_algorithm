from itertools import combinations_with_replacement


def judgeWinner(c, info):
    ryan = [0] * 11
    for i in c:
        ryan[10 - i] += 1
    winner = 0
    loser = 0
    for i in range(len(ryan)):
        if info[i] == 0 and ryan[i] == 0:
            continue
        if info[i] >= ryan[i]:
            loser += 10 - i
        else:
            winner += 10 - i

    # print(ryan)
    if winner > loser:
        ryan.append(winner - loser)
        result.append(ryan)


def solution(n, info):
    global result
    storage = []
    result = []
    comb = list(combinations_with_replacement(range(11), n))
    comb.sort(reverse=True)
    for c in comb:
        judgeWinner(c, info)
    # print(result)
    if len(result) == 0:
        return [-1]

    # for i in result:
    #     print(i[11])
    # result.sort(key=lambda x:-x[11])
    # MAX=result[0][-1]
    # print(MAX)
    # for i in result:
    #     if i[-1]==MAX:
    #         storage.append(i[:-1])
    #     else:
    #         break
    # print(storage)

    result.sort(key=lambda x: (-x[11], -x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
    MAX = result[0][-1]
    for i in result:
        if i[-1] == MAX:
            print(i)
    # print(result)

    # print(result[0][:-1])
    return result[0][:-1]

    # print(MAX)
    # print(result)