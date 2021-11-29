import time


def nquery(query):
    q = []
    for j in query:
        for k in range(len(j) - 1, len(j) - 8, -1):
            if j[k] == " ":
                tmp = []
                idx = k
                a = list(map(str, j[:idx].split()))
                for t in a:
                    if t != "and":
                        tmp.append(t)
                tmp.append(int(j[idx + 1:]))
                q.append(tmp)
                break
    return q


def checker(query, candidate):
    # print(q,candidate)
    if query[0] == "-" and query[1] == "-" and query[2] == "-" and query[3] == "-":
        return True
    if "-" in query:
        q = query[:]
        for i in range(4):
            if q[i] == "-":
                q[i] = candidate[i]
        if q[:4] == candidate[:4]:
            return True
        else:
            return False
    else:
        if query[:4] == candidate[:4]:
            return True
        else:
            return False

        # for in range
    for i in range(4):
        if query[i] == "-":
            continue
        elif query[i] != "-" and query[i] != candidate[i]:
            return False

    return True


def solution(info, query):
    start = time.time()
    candidates = []
    answer = []
    for i in info:
        member = list(i.split())
        member[4] = int(member[4])
        candidates.append(member)
    queries = nquery(query)
    candidates.sort(key=lambda x: -x[4])
    # queries.sort(key=lambda x: x[4])
    for i in queries:
        a = i.pop()
        # print(a)
        cnt = 0
        for j in candidates:
            # print(a,b)
            if a > j[4]:
                break
            if checker(i, j):
                # print(i,j)
                cnt += 1
                # print(cnt)
        answer.append(cnt)
    # print("time :", time.time() - start)
    return answer