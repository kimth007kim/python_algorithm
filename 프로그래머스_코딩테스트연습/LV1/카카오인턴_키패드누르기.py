def abscalc(a, b):
    if a > b:
        return a - b
    else:
        return b - a


def find(button, num):
    for i in range(4):
        for j in range(3):
            if num == button[i][j]:
                return i, j


def solution(numbers, hand):
    answer = ''
    button = [[1] * 3 for _ in range(4)]
    cal = 0
    for i in range(len(button)):
        for j in range(len(button[0])):
            button[i][j] = int(button[i][j]) + cal
            cal += 1
    button[3][0] = "*"
    button[3][1] = 0
    button[3][2] = "#"
    lx, ly = 3, 0
    rx, ry = 3, 2

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            lx, ly = find(button, num)
            answer += "L"
        elif num == 3 or num == 6 or num == 9:
            rx, ry = find(button, num)
            answer += "R"
        else:
            tx, ty = find(button, num)
            print(tx, ty)
            lres = 0
            rres = 0
            lres += abscalc(tx, lx)
            lres += abscalc(ty, ly)
            rres += abscalc(tx, rx)
            rres += abscalc(ty, ry)
            if rres > lres:
                lx, ly = tx, ty
                answer += "L"
            if lres > rres:
                rx, ry = tx, ty
                answer += "R"
            if lres == rres:
                if hand == "right":
                    rx, ry = tx, ty
                    answer += "R"
                else:
                    lx, ly = tx, ty
                    answer += "L"
    return answer
