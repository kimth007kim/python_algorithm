def find(parents, money, number, answer):
    print(parents, money, number, answer)
    print("parents[number]  =", parents[number])
    if parents[number] == number or money // 10 == 0:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    print("number,answer[number]", number, answer[number])
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    print("enroll", enroll)
    print("referral", referral)
    print("seller", seller)
    print("amount", amount)
    n = len(enroll)
    answer = [0] * (n + 1)
    d = {}
    parents = [i for i in range(n + 1)]
    print("초기parents= ", parents)
    for i in range(n):
        d[enroll[i]] = i + 1
    print("d          = ", d)
    # print(referral)
    for i in range(n):
        if referral[i] == "-":
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    # print(seller)
    print("변경parents= ", parents)
    for i in range(len(seller)):
        print(amount[i])
        print(d[seller[i]])

        find(parents, amount[i] * 100, d[seller[i]], answer)
    return answer[1:]