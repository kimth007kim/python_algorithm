def find(parents, money, number, answer):
    if money // 10 == 0 or parents[number] == number:
        answer[number] += money
        return
    send = money // 10
    mine = money - send
    answer[number] += mine
    find(parents, send, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    print("enroll", enroll)
    print("referral", referral)
    print("seller", seller)
    print("amount", amount)
    n = len(enroll)
    parents = [i for i in range(n + 1)]
    d = {}
    for i in range(n):
        d[enroll[i]] = i + 1
    for i in range(n):
        if referral[i] == "-":
            parents[i + 1] = 0
        else:
            parents[i + 1] = d[referral[i]]
    answer = [0] * (n + 1)
    for i in range(len(seller)):
        find(parents, amount[i] * 100, d[seller[i]], answer)
        # print(seller[i],amount[i])

    # print(answer)
    return answer[1:]