def findline(board, move):
    move -= 1
    for i in range(len(board)):
        # print(board[i][move])
        if board[i][move] != 0:
            target = board[i][move]
            board[i][move] = 0
            return target
    return -1


def box_delete(box):
    last = box[len(box) - 1]
    last2 = box[len(box) - 2]
    if last == last2:
        box.pop()
        box.pop()
        return True
    return False


def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        target = findline(board, i)
        if target != -1:
            box.append(target)
            if len(box) >= 2:
                if box_delete(box) == True:
                    answer += 2
    return answer