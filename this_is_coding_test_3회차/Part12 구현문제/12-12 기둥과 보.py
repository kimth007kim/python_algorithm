def buildCheck(x, y, a, answer):
    # x = x 좌표
    # y = y 좌표
    # a = 0: 기둥 1: 보
    # b = 0: 삭제 1: 설치

    # 기둥 설치
    if a == 0:
        if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
            return True
    # 보 설치
    else:
        if (x + 1, y - 1, 0) in answer or (x, y - 1, 0) in answer or (
                (x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
            return True
    return False


def solution(n, build_frame):
    answer = []
    gi = []
    bo = []
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            canswer = answer[:]
            if (x, y, a) in answer:
                answer.remove((x, y, a))
            for tx, ty, ta in answer:
                if not buildCheck(tx, ty, ta, answer):
                    answer = canswer
        # 설치
        if b == 1:
            canswer = answer[:]
            answer.append((x, y, a))
            for tx, ty, ta in answer:
                if not buildCheck(tx, ty, ta, answer):
                    answer = canswer
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer