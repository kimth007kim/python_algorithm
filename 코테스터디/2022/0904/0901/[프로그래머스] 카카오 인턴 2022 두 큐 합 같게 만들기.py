def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    target = (s1 + s2) // 2
    print(s1, s2)

    i, j, length = 0, 0, len(queue1)
    cnt = 0
    while i < length * 2 and j < length * 2:
        if s1 > target:
            s1 -= queue1[i]
            s2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
            cnt += 1
        if s1 < target:
            s1 += queue2[j]
            s2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
            cnt += 1
        if s1 == target:
            return cnt

    return -1