from itertools import combinations


def calc(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def check(data, people):
    comb = combinations(people, 2)
    for p1, p2 in list(comb):
        x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
        distance = calc(x1, x2) + calc(y1, y2)
        if distance > 2:
            continue
        else:
            if x1 == x2:
                if y1 > y2:
                    tm = y1 - 1
                else:
                    tm = y2 - 1
                if data[x1][tm] == "X":
                    continue
                else:
                    print("칸은 하나인데 거리를 위반하는구나", p1, p2)
                    return False
            elif y1 == y2:
                if x1 > x2:
                    tm = x1 - 1
                else:
                    tm = x2 - 1
                if data[tm][y1] == "X":
                    continue
                else:
                    print("칸은 하나인데 거리를 위반하는구나", p1, p2)
                    return False

            else:
                if data[x1][y2] == "X" and data[x2][y1] == "X":
                    continue
                else:
                    return False
    return True
    # print(p1,p2)

    # |r1 - r2| + |c1 - c2|
    # print(p1,p2)
    # print(distance)
    # print(data)
    # print(people)


def solution(places):
    answer = [1] * 5
    room = []
    for i in range(len(places)):
        tmp = []
        for j in places[i]:
            tmp.append(list(j))
        room.append(tmp)

    for a in range(5):
        people = []
        for i in range(5):
            for j in range(5):
                if room[a][i][j] == "P":
                    people.append((i, j))
        if not check(room[a], people):
            answer[a] = 0
        # print()
    return answer