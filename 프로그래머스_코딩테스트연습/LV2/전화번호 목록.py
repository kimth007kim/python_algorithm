def solution(phone_book):
    MIN = int(1e9)
    for i in phone_book:
        MIN = min(MIN, len(i))
    dic = {}
    for i in phone_book:
        for j in range(MIN, len(i)):
            print(i[:j])
            dic[i[:j]] = 0
    # print(dic)

    for i in phone_book:
        if i in dic:
            return False
    return True