
def self_num():
    a=1
    nlist= []
    for i in range(10000):
        nlist.append(i+1)

    while a <= 10000:
        res = 0
        # 10보다 작으면 그냥 둘이더하고
        if a < 10:
            res = a+a

        # 10보다 크면 자리수 나눠서 더함
        elif a >= 10 and a < 100:
            n1 = a //10
            n2 = a %10
            res= a +n1+ n2
        elif a >= 100 and a< 1000:
            n1= a // 100
            n2= (a- n1*100)//10
            n3= a-n1*100-n2*10
            res= a+ n1+ n2+n3

        elif a >=1000 and a< 100000:
            n1= a // 1000
            n2= (a - n1*1000)//100
            n3= (a - n1*1000 - n2*100)//10
            n4= a - n1*1000 - n2*100 - n3*10
            res= a+ n1+ n2+ n3+ n4

        if res<= 10000 and res in nlist:
            nlist.remove(res)

        a += 1

    for i in nlist:
        print(i)

self_num()