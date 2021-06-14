def solution(words, queries):
    answer = [0 for _ in range(len(queries))]
    nqueries = []
    for i in range(len(queries)):
        if queries[i][0] == "?":
            n = 0  # 앞에 ?
        else:
            n = 1  # 뒤에 ?
        c = queries[i].count("?")
        nqueries.append((n, c, len(queries[i]), queries[i]))
    nwords = []
    for i in range(len(words)):
        nwords.append((len(words[i]), words[i]))
    for i in range(len(nqueries)):
        ncnt = 0
        for j in range(len(nwords)):
            n, cnt, l, q = nqueries[i]
            if nqueries[i][2] != nwords[j][0]:
                continue
            if n == 0:
                if q[cnt:] == nwords[j][1][cnt:]:
                    answer[i] += 1
            if n == 1:
                if q[:(l - cnt)] == nwords[j][1][:(l - cnt)]:
                    answer[i] += 1

    return answer