def solution(record):
    result = []
    answer = []
    user = []
    Length = len(record)
    for i in range(Length):
        tmp = record[i].split()
        if tmp[0] == "Enter":
            if tmp[1] not in user:
                user.append(tmp[1])
            result.append([tmp[1], tmp[2], 0])
        if tmp[0] == "Leave":
            result.append([tmp[1], "", 1])
        if tmp[0] == "Change":
            result.append([tmp[1], tmp[2], 2])

    for i in range(len(user)):
        finduser(user[i], result)

    # for uid,name in user:
    #     changer(uid,name,result)

    print(result)

    for i in range(len(result)):
        if result[i][2] == 0:
            string = result[i][1] + "님이 들어왔습니다."
            answer.append(string)
        elif result[i][2] == 1:
            string = result[i][1] + "님이 나갔습니다."
            answer.append(string)
    return answer


def finduser(user, result):
    name = ""
    for i in range(len(result) - 1, -1, -1):
        if user == result[i][0] and (result[i][2] == 2 or result[i][2] == 0):
            name = result[i][1]
            break
    for i in range(len(result)):
        if result[i][0] == user and result[i][1] != name:
            result[i][1] = name
