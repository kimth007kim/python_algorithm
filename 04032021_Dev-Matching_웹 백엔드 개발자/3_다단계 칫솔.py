enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller=["young", "john", "tod", "emily", "mary"]
amount=[12, 4, 2, 5, 10]
result=[360, 958, 108, 0, 450, 18, 180, 1080]


def cal(name, price):
    global name_dic
    remain_price = 0 if int(price * 0.1) < 1 else int(price * 0.1)
    print(remain_price)
    self_price = price - remain_price

    name_dic[name][1] += self_price
    up_name = name_dic[name][0]
    if up_name == '':
        return
    cal(up_name, remain_price)


def solution(enroll, referral, seller, amount):
    global name_dic

    name_dic = {}

    for e, r in zip(enroll, referral):
        name_dic[e] = ['', 0]
        if r != '-':
            name_dic[e][0] = r

    for s, a in zip(seller, amount):
        price = a * 100
        cal(s, price)

    answer = [v[1] for k, v in name_dic.items()]
    return answer

print(solution(enroll,referral,seller,amount))
