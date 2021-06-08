def solution(record):
    answer = []
    user = {}
    print(user)
    for message in record:
        if (message.split(' ')[0] == 'Enter') or (message.split(' ')[0] == 'Change'):
            user[message.split(' ')[1]] = message.split(' ')[2]

    for message in record:
        if message.split(' ')[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user[message.split(' ')[1]]))
        elif message.split(' ')[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(user[message.split(' ')[1]]))
        # else:
        #     pass

    return answer