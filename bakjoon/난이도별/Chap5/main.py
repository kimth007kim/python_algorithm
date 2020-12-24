total = int(input())
avg = []

for i in range(total):
    sco = list(map(int, input().split()))
    num = sco[0]
    del sco[0]
    sum=0
    score= 0
    cnt = 0

    for n in sco:
        sum+=n
    score=sum/num

    for i in range(len(sco)):
        if score< sco[i]:
            cnt += 1

    aa = cnt/num*100
    avg.append(format(aa,".3f"))


for n in avg:
    print(n+"%")