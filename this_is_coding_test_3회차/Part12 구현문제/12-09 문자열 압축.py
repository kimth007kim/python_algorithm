def solution(s):
    LEN = len(s)
    # f=LEN//2
    if len(s) == 1:
        return 1
    MIN = int(1e9)
    for i in range(1, LEN // 2 + 1):
        prev = s[:i]
        previous = i
        result = ""
        cnt = 1
        for j in range(i + i, LEN + 1, i):
            now = s[previous:j]

            if now == prev:
                cnt += 1
            else:
                if cnt > 1:
                    # result+=previous
                    result += str(cnt) + prev
                else:
                    result += prev
                cnt = 1
            previous = j
            prev = now
        #

        if prev == s[previous - 2 * i:previous - i]:
            result += str(cnt) + prev
        else:
            result += prev
        # print(result,"    ",prev,s[previous-2*i:previous-i])
        if j < LEN:
            result += s[j:]
        MIN = min(MIN, len(result))
    answer = 0
    return MIN