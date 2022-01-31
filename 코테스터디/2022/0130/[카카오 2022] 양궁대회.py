from itertools import combinations_with_replacement


def judge(ap, ry, win):
    appeach = 0
    ryan = 0
    for i in range(11):
        if ap[i] == ry[i] and ap[i] == 0:
            continue
        if ap[i] >= ry[i]:
            appeach += 10 - i
        elif ap[i] < ry[i]:
            ryan += 10 - i
    if appeach < ryan:
        win.append([ry, ryan - appeach])


def convert(shot):
    result = [0] * 11
    for i in shot:
        result[10 - i] += 1
    return result


def solution(n, info):
    comb = list(combinations_with_replacement(range(11), n))
    comb.sort(reverse=True)
    win = []
    for t in comb:
        shot = convert(t)
        judge(info, shot, win)
    if len(win) == 0:
        return [-1]
    win.sort(key=lambda x: -x[1])
    MAX = win[0][1]
    result = []
    for arr, num in win:
        if num != MAX:
            break
        result.append(arr)
    result.sort(key=lambda x: (-x[10], -x[9], -x[8], -x[7], -x[6], -x[5], -x[4], -x[3], -x[2], -x[1], -x[0]))
    return result[0]