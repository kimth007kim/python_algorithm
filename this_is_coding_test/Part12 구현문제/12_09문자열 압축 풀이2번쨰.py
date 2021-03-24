def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        compressed = ""
        count = 1
        prev = s[0:i]
        for j in range(i, i + len(s), i):
            if s[j:j + i] == prev:
                count += 1
            else:
                if count != 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j + i]
                count = 1
        answer = min(answer, len(compressed))
        print(answer)

    return answer