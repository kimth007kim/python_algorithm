n=12
weak=[1, 5, 6, 10]
dist=[1, 2, 3, 4]

def solution(n, weak, dist):
    cnt = 0
    for distance in dist:
        fundist(distance, weak, n)
        cnt += 1
    answer = 0
    return answer


def fundist(distance, weak, n):
    nweak = []
    for i in range(len(weak)):
        nweak.append(weak[i])
        nweak.append(weak[i] + n)
    nweak.sort()
    count = len(weak)-1
    while count>0:
        for i in range(len(weak)):
            if distance >= nweak[i + count] - nweak[i]:
                print()
                # for j in range()
        # count-=1

    # print(nweak)
solution(n, weak, dist)