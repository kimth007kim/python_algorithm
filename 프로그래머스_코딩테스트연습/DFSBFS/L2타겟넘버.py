numbers	=[1, 1, 1, 1, 1]
target=3


def solution(numbers, target):
    length = len(numbers)

    count = 0

    def dfs(cnt, word):
        nonlocal count
        if cnt == length:
            if target == word:
                count += 1
            return

        for i in range(2):
            if i == 0:
                dfs(cnt + 1, word + numbers[cnt])
            else:
                dfs(cnt + 1, word - numbers[cnt])

    dfs(0, 0)

    answer = count
    return answer


print(solution(numbers,target))