def set_array(arr):
    cnt = list(set(arr))

    return len(cnt)


def solution(gems):
    target = set_array(gems)
    array = []
    for start in range(len(gems)):
        for end in range(start + target - 1, len(gems)):
            interval_sum = set_array(gems[start:end + 1])
            if interval_sum == target:
                array.append([end - start, start + 1, end + 1])
                break
    array.sort(key=lambda x: (x[0], x[1]))
    return [array[0][1], array[0][2]]