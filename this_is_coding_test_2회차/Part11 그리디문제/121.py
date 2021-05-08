places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
def solution(places):
    for tmp in places:
        people = []
        part = []
        for col in range(5):
            data = list(tmp[col])

        for i in range(5):
            for j in range(5):
                if data[i][j] == "P":
                    people.append((i, j))
                elif data[i][j] == "X":
                    part.append((i, j))
        print(people, part)
    answer = []
    return answer

print(solution(places))