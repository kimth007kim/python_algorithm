def calc(n, arr, MAX):
    while n > 0:
        if MAX == 0:
            return arr
        for i in range(len(arr)):
            if arr[i] == MAX:
                arr[i] -= 1
                n -= 1
                if n == 0:
                    return arr
            elif arr[i] != MAX:
                MAX = arr[i]
                break
    return arr


def make_answer(arr):
    total = 0
    for i in arr:
        total += i ** 2
    return total


def solution(n, works):
    works.sort(reverse=True)
    maximum = works[0]
    result = calc(n, works, maximum)
    answer = make_answer(result)

    return answer