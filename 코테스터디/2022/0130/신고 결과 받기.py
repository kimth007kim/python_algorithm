def solution(id_list, report, k):
    user = {}
    reported = {}
    for i in id_list:
        user[i] = []
        if i not in reported:
            reported[i] = 0
    answer = []

    for i in report:
        a, b = i.split()
        user[b].append(a)

    for i in user:
        tmp = list(set(user[i]))
        # print(tmp)
        if len(tmp) >= k:
            for i in tmp:
                reported[i] += 1
    for i in id_list:
        answer.append(reported[i])

    return answer