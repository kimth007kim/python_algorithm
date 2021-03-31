def solution(n, build_frame):
    data = [[0] * (n + 5) for _ in range(n + 5)]

    for i in range(len(build_frame)):
        x, y, a, b = build_frame.pop(0)
        # if a==0 and b==0:
        #     degi(x,y)
        # if a==1 and b==0:
        #     debo(x,y)
        if a == 0 and b == 1:
            addgi(x, y, n, data)
        if 1 == 0 and b == 1:
            addbo(x, y, n, data)
    for i in data:
        print(i)
    answer = [[]]
    return answer


# def degi(x,y):

# def debo(x,y):

def addgi(x, y, n, data):
    if x + 1 <= n:
        data[n - x][n - y] = 1
        data[n - x + 1][n - y] = 1


def addbo(x, y, n, data):
    if y + 1 <= n:
        data[n - x][n - y] = 1
        data[n - x][n - y + 1] = 1