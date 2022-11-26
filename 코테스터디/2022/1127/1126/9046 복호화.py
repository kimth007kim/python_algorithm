from collections import defaultdict

t = int(input())
for i in range(t):
    dic =defaultdict(int)
    tmp = list(map(str,input()))
    for j in tmp:
        if j ==" ":
            continue
        dic[j]+=1

    MAX=0
    flag= False
    answer= ""
    for j in dic:
        if dic[j]>MAX:
            flag=True
            MAX=dic[j]
            answer=j
        elif dic[j]==MAX:
            flag=False
    if flag==True:
        print(answer)
    else:
        print("?")