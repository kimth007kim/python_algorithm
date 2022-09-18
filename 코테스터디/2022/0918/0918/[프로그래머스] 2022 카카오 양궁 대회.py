from itertools import combinations_with_replacement

def judge(apeach, lion_arr):
    global cand, MAX
    me, you = 0, 0
    lion = [0] * 11
    for i in lion_arr:
        lion[i] += 1
    for i in range(11):
        if apeach[i] == 0 == lion[i]:
            continue
        if apeach[i] >= lion[i]:
            you += 10 - i
        else:
            me += 10 - i
    if me > you:
        total = me - you
        if total > MAX:
            MAX = total
            cand = [lion]
        elif total == MAX:
            cand.append(lion)

def solution(n, info):
    global N, cand, MAX
    N = n
    cand = []
    MAX = 0
    comb = combinations_with_replacement(range(11), n)
    for infos in list(comb):
        judge(info, infos)
    if len(cand) == 0:
        return [-1]
    cand.sort(key=lambda x: (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))

    return cand[0]