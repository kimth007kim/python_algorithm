logs=["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
adv_time="25:00:00"
play_time="99:59:59"


def checktime(word, all_time):
    result = 0
    time1, time2 = word.split("-")
    t1 = findsecond(time1)
    t2 = findsecond(time2)
    all_time[t1] = t2
    fpoint.append(t1)
    bpoint.append(t2)


def findsecond(word):
    second = 0
    hr, mn, sc = word.split(":")
    hr, mn, sc = int(hr), int(mn), int(sc)
    second += sc
    second += mn * 60
    second += hr * 3600

    return second

def secondtoword(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    global bpoint, fpoint
    all_time = {}
    new_time = {}
    fpoint = []
    bpoint = []

    adv = findsecond(adv_time)
    play = findsecond(play_time)
    fpoint.append(0)
    bpoint.append(play)

    answer = ''
    for i in logs:
        checktime(i, all_time)
    for i in fpoint:
        if i + adv <= play:
            new_time[i] = i + adv
    for i in bpoint:
        if i - adv >= 0:
            new_time[i - adv] = i
    # new_time = sorted(new_time.items())
    result = [0] * (len(new_time))

    counter = 0
    for i in new_time:
        # for i in range(len(new_time)):
        s1, e1 = i, i + adv
        for s2, e2 in all_time.items():
            print(s1, e1, "---------------", s2, e2)
            if s1<s2 and e1>e2:
                result[counter]+=e2-s2
                continue
            if s2<s1 and e2>e1:
                result[counter]+=e1-s1
            if s2==s1:
                result[counter]+=min(e1-s1,e2-s1)
            elif s2>s1:
                if s2>e1:
                    continue
                else:
                    result[counter]+=e1-s2
            elif s1>s2:
                if s1>e2:
                    continue
                else:
                    result[counter]+=e2-s1

            # if e1 > s2 and e2 > s1:
            #     result[counter] += min(e1 - s2, e2 - s1)
            # elif e1 > s2:
            #     result[counter] += e1 - s2
            # elif e2 > s1:
            #     result[counter] += e2 - s1
            print(result)
        counter += 1
    counter = 0
    value = 0
    box = {}
    minimum=int(1e9)
    for i in new_time:
        print(result[counter])
        if value <= result[counter]:
            if minimum>i:
                box["time"] = i
                minimum=i
                value = result[counter]
        # counter += 1
    print("minimum",minimum)


    print(box)
    print(new_time)
    print(result)

    return answer


solution(play_time,adv_time,logs)