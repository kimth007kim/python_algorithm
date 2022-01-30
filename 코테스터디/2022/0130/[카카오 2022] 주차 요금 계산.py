from collections import deque


def time_to_int(time):
    hr, mm = time.split(":")
    result = int(hr) * 60 + int(mm)
    return result


def calc_total(time, general_time, general_fee, extra_time, extra_fee):
    if general_time >= time:
        return general_fee
    tmp = time - general_time
    if tmp % extra_time == 0:
        tmp = tmp // extra_time
    else:
        tmp = tmp // extra_time + 1

    tmp *= extra_fee
    tmp += general_fee
    return tmp


def solution(fees, records):
    general_time, general_fee, extra_time, extra_fee = fees
    IN = {}
    OUT = {}
    TOTAL = {}
    idx = []
    answer = []
    for i in records:
        time, number, types = i.split()
        if number not in idx:
            idx.append(number)
            IN[number] = deque()
            OUT[number] = deque()
            TOTAL[number] = 0
        minutes = time_to_int(time)
        if types == "IN":
            IN[number].append(minutes)
        else:
            OUT[number].append(minutes)

    for i in idx:
        if len(OUT[i]) != len(IN[i]):
            OUT[i].append(1439)
        while IN[i]:
            tmp_in = IN[i].popleft()
            tmp_out = OUT[i].popleft()
            TOTAL[i] += tmp_out - tmp_in
    idx.sort()
    for i in idx:
        fee = calc_total(TOTAL[i], general_time, general_fee, extra_time, extra_fee)
        answer.append(fee)

    return answer