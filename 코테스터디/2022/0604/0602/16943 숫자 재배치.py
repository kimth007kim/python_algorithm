from itertools import permutations

a,b = list(input().split())
target =int(b)

answer=-1

comb = permutations(a,len(a))
for i in list(comb):
    if i[0]!="0":
        tmp = int("".join(list(i)))
        if target> tmp:
            answer= max(answer,tmp)

print(answer)
