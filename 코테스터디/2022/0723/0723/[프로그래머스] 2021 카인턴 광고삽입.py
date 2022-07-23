def int_to_time(time):
    result = ""

    def zeroMaker(t):
        if len(t) == 1:
            return "0" + t
        return t

    hr = str(time // 3600)
    time = time % 3600
    mm = str(time // 60)
    ss = str(time % 60)
    result += zeroMaker(hr) + ":" + zeroMaker(mm) + ":" + zeroMaker(ss)
    return result


def time_to_int(time):
    result = 0
    hh, mm, ss = time.split(":")
    result += int(hh) * 3600 + int(mm) * 60 + int(ss)
    return result


def solution(play_time, adv_time, logs):
    play = time_to_int(play_time)
    adv = time_to_int(adv_time)
    dp = [0] * (play + 1)

    for i in logs:
        _s, _e = i.split("-")
        s, e = time_to_int(_s), time_to_int(_e)
        dp[s] += 1
        dp[e] -= 1
    print(play)

    for i in range(1, len(dp)):
        dp[i] += dp[i - 1]
    MAX = 0
    length = 0
    prefix = 0
    point = 0
    start = 0

    for i in range(len(dp)):
        prefix += dp[i]
        length += 1
        if length == adv:
            if MAX < prefix:
                MAX = prefix
                point = start
            prefix -= dp[start]
            start += 1
            length -= 1

    answer = ''
    return int_to_time(point)
