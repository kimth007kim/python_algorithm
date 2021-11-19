def transform(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return transform(q, base) + T[r]


def solution(n, t, m, p):
    print(transform(14, 16))
    answer = ''
    total = t * m
    word = ""
    for i in range(total):
        word += transform(i, n)

    cnt = 1
    for i in range(len(word)):
        if cnt == p:
            answer += word[i]
            if len(answer) == t:
                break
        cnt += 1
        if cnt > m:
            cnt = 1

    return answer

print(solution())