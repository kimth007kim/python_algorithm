def solution(n, k, cmd):
    def makeList(dic, state, stack, LENGTH):
        cnt = 0
        LENGTH -= 1
        for i in dic:
            if dic[i] == True:
                cnt += 1
            if cnt == state + 1:
                dic[i] = False
                stack.append(i)
                break
        return i

    LENGTH = n
    state = k
    dic = {}
    stack = []
    for i in range(n):
        dic[i] = True

    for com in cmd:
        if len(com) == 1:
            if com == "C":
                makeList(dic, state, stack, LENGTH)
            else:
                word = stack.pop()
                dic[word] = True
        else:
            com, number = com.split()
            number = int(number)
            if com == "D":
                if state + number < LENGTH:
                    state += number
            if com == "U":
                if state - number >= 0:
                    state -= number

    answer = ''
    for i in dic:
        if not dic[i]:
            answer += "X"
        else:
            answer += "O"
    return answer