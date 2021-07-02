def find(parents,money,number,answer):
    print(parents,money,number,answer)
    if parents[number]==number or money // 10==0:
        answer[number]+=money
        return
    send =money //10


def solution(enroll, referral, seller, amount):
    n= len(enroll)
    answer = [0]*(n+1)
    d={}
    parents=[i for i in range(n+1)]
    # print(parents)
    for i in range(n):
        d[enroll[i]]=i+1
    # print(d)
    # print(referral)
    for i in range(n):
        if referral[i]=="-":
            parents[i+1]=0
        else:
            parents[i+1]=d[referral[i]]
    print(seller)
    for i in range(len(seller)):
        find(parents,amount[i]*100,d[seller[i]],answer)
    return answer[1:]