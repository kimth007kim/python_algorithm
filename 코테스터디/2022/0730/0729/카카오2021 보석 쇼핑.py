def dict_check(visited):
    if len(visited) == target:
        return True
    return False


def visited_add(visited, num):
    if num not in visited:
        visited[num] = 1
    else:
        visited[num] += 1


def visited_minus(visited, num):
    visited[num] -= 1
    if visited[num] == 0:
        del visited[num]


def solution(gems):
    global target
    idx = {}
    answer = []
    target = len(list(set(gems)))
    visited = {}
    _start, _end = 0, 0
    length = int(1e9)

    start = 0
    for end in range(len(gems)):
        visited_add(visited, gems[end])

        if dict_check(visited) == True:
            if length > end - start + 1:
                _start, _end = start, end
                length = end - start + 1
            while dict_check(visited) == True:
                visited_minus(visited, gems[start])
                start += 1
                if length > end - start + 1 and dict_check(visited) == True:
                    _start, _end = start, end
                    length = end - start + 1
    return [_start + 1, _end + 1]
