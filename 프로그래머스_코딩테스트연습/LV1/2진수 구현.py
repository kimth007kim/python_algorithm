n= int(input())
def solution(n):
    answer = ''
    result = 0

    while n >= 1:
        rest = n % 2
        n //= 2
        answer += str(rest)
    print(answer)

    # i = 0
    # for idx in range(len(answer)-1, -1, -1):
    #     result += int(answer[idx]) * (3**i)
    #     i += 1
    # return result
    return answer


print(solution(n))