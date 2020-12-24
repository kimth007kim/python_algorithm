num = int(input())
nlist= []
for i in range(num):
    n1 = input()
    total=0
    score=1
    for i in range(len(n1)):
        if n1[i]=="O":
            if n1[i-1] == "O" and i>0:
                score+=1
                total += score
            else:
                total += score
        else:
            score=1
    nlist.append(total)

for i in nlist:
    print(i)