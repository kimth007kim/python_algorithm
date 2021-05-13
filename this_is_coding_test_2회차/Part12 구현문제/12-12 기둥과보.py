n=5
build_frame=[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def solution(n, build_frame):
    gi = []
    bo = []
    for i in build_frame:
        x, y, a, b = i
        if a == 1 and b == 1:
            createbo(x, y, gi, bo)
        if a == 0 and b == 1:
            creategi(x, y, gi, bo)
        if a == 1 and b == 0:
            deletebo(x, y, gi, bo)
        if a == 0 and b == 0:
            deletegi(x, y, gi, bo)

    print("gi:", gi)
    print("bo:", bo)
    answer = [[]]
    return answer


def createbo(x, y, gi, bo):
    if ((x, y - 1) in gi or (x + 1, y - 1) in gi) or ((x - 1, y) in bo and (x + 1, y) in bo):
        bo.append((x, y))


def creategi(x, y, gi, bo):
    if y == 0 or (x, y - 1) in gi or (x, y) in bo or (x - 1, y) in bo:
        gi.append((x, y))


def deletebo(x, y, gi, bo):
    print()


def deletegi(x, y, gi, bo):
    print()