def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    # 끝나는 숫자 구하기
    number = 0
    for i in range(1, n + 1):
        number += i
    start = 1
    data = []
    for i in range(n):
        tmp = [0 for _ in range(i + 1)]
        data.append(tmp)

    # 초기방향,x,y 설정
    direction = 0
    x = 0
    y = 0
    length = n

    def turn(start, direction, x, y, length):
        if length != n:
            direction = (direction + 1) % 3
            x += dx[direction]
            y += dy[direction]

        for i in range(length):
            if i != 0:
                x += dx[direction]
                y += dy[direction]
            data[x][y] = start
            start += 1
        length -= 1

        return start, direction, x, y, length

    #     for i in range(length):
    #         if i!=0:
    #             x+=dx[direction]
    #             y+=dy[direction]
    #         data[x][y]=start
    #         start+=1

    while start <= number:
        # for i in range(2):
        start, direction, x, y, length = turn(start, direction, x, y, length)

    # for i in data:
    #     print(i)

    # print("x={} y={} start={}".format(x,y,start))
    answer = []
    for i in data:
        for j in i:
            answer.append(j)

    # print(answer)

    return answer