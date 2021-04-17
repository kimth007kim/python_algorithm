def solution(N, stages):
    # print(1/8,3/7,2/4,1/2,0/1)
    people = len(stages)
    answer = []
    for i in range(1, N + 1):
        cnt = 0
        for j in range(len(stages)):
            if i == stages[j]:
                cnt += 1

        # print(cnt,"  ",people)
        if people == 0:
            answer.append((i, 0))
        else:
            answer.append((i, cnt / people))
        people -= cnt
    # print(answer)
    answer.sort(key=lambda x: (-x[1], x[0]))

    result = []
    for j in answer:
        result.append(j[0])
    return result