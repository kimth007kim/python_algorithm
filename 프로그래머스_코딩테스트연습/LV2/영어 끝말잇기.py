import math


def solution(n, words):
    answer = []
    log = {}
    number = 0
    turn = 0

    previous = ""
    for i in range(len(words)):
        now = words[i]
        if words[i] in log or (i != 0 and previous[-1] != now[0]):
            number = ((n + i) % n) + 1
            turn = math.ceil((i + 1) / n)
            break
        log[words[i]] = 1
        previous = now
    answer.append(number)
    answer.append(turn)
    return answer