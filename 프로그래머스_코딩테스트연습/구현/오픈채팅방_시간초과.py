def solution(record):
    result = []
    answer = []
    Length = len(record)
    for i in range(Length):
        tmp = record[i].split()
        if tmp[0] == "Enter":
            EnterName(result, tmp[1], tmp[2])
        if tmp[0] == "Leave":
            leaveName(result, tmp[1])
        if tmp[0] == "Change":
            changeName(result, tmp[1], tmp[2])

    for i in range(len(result)):
        if result[i][2] == 0:
            string = str(result[i][1]) + "님이 들어왔습니다."
        else:
            string = str(result[i][1]) + "님이 나갔습니다."
        answer.append(string)

    return answer


def EnterName(result, uid, name):
    result.append([uid, name, 0])
    length = len(result)
    for i in range(length):
        if uid == result[i][0] and name != result[i][1]:
            result[i][1] = name


def leaveName(result, uid):
    length = len(result)
    name = ""
    for i in range(length - 1, -1, -1):
        if uid == result[i][0]:
            name = result[i][1]
            break
    result.append([uid, name, 1])


def changeName(result, uid, name):
    length = len(result)
    for i in range(length):
        if uid == result[i][0]:
            result[i][1] = name

# def EnterName(result,x,y):
#     lresult=len(result)
