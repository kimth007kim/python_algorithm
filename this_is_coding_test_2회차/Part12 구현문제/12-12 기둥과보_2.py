def check(answer):
    for x, y, stuff in answer:
        if stuff == 0:  # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
            # 보 한쪽 윗부분에 있거나 2,1,0 1,1,1 2,1,1 (x-1,y,1) (x,y,1)
            # 또 다른 기둥에 있어야한다. x,y-1,0
        if stuff == 1:  # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False

            # 한쪽 끝 부분이 기둥위에 있거나 2,2,1  2,1,0  3,1,0 x,y-1,0  x+1,y-1,0
            # 양쪽 끝 부분이 다른 보와 동시에 연결 3,2,1 2,2,1 4,2,1 x-1,y,1  x+1,y,1
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame: 
        x, y, a, b = i
        if b == 1:  # 설치
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])

        if b == 0:  # 삭제
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    print(answer)

    return sorted(answer)