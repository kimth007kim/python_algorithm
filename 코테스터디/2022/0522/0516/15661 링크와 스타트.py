from itertools import combinations


def count_score(arr,data):
    score=0
    for i in arr:
        for j in arr:
            score+=data[i][j]
    return score


n= int(input())
data=[]
original=set([i for i in range(n)])
# print(original)
for i in range(n):
    data.append(list(map(int,input().split())))
MIN=1e9



for i in range(1,n//2+1):
    comb = combinations(range(n),i)
    for team in comb:
        opponent = original-set(team)
        result =abs(count_score(team,data)-count_score(opponent,data))
        MIN=min(MIN,result)

print(MIN)