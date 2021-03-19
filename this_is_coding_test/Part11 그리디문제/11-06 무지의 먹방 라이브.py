def solution(food_times, k):
    # 회전판에 먹어야 할 음식 N개 1~N 일정시간이 소요된다.
    # K=중단된시간 FOOTIMES=모든음식을 먹는데 필요한시간
    cnt = 0
    k += 1
    flen = len(food_times)
    fo = [0] * (flen + 1)
    for i in range(flen):
        fo[i + 1] = food_times[i]

    while k > 0:
        for i in range(1, flen + 1):
            cnt = 0
            if fo[i] == 0:
                continue
            else:
                fo[i] = fo[i] - 1
                k -= 1
                cnt = i
            if k == 0:
                return cnt

        for j in range(1, flen + 1):
            ddcnt = 0
            if fo[i] == 0:
                ddcnt += 1
            if ddcnt == flen:
                return -1
