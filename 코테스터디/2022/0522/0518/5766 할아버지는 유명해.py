from collections import defaultdict

answer=[]
def calc(n,m,answer):
    arr= []
    MAX=-1
    NEXT=-1
    player=defaultdict(int)
    for i in range(n):
        tmp=list(map(int,input().split()))
        for j in tmp:
            player[j]+=1
            MAX=max(MAX,player[j])

    for i in player:
        if player[i]==MAX:
            continue
        NEXT= max(NEXT,player[i])

    for i in player:
        if player[i]==NEXT:
            arr.append(i)

    arr.sort()
    answer.append(arr)

while True:
    n,m= map(int,input().split())
    if n==0 and m==0:
        break
    calc(n,m,answer)

for i in answer:
    print(*i)
