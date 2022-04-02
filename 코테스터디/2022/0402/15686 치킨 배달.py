from itertools import combinations
import sys
input =sys.stdin.readline
def calc(a,b,c,d):
    result=0
    if a>c:
        result+=a-c
    else:
        result+=c-a
    if b>d:
        result+=b-d
    else:
        result+=d-b
    return result

def short_distance(house,arr):
    result=0
    for a,b in house:
        value=int(1e9)
        for c,d in arr:
            tmp=calc(a,b,c,d)
            if value>tmp:
                value=tmp
        result+=value
    return result

n,m= map(int,input().split())
graph=[]

chicken=[]
house=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j]==1:
            house.append([i,j])
        if tmp[j]==2:
            chicken.append([i,j])
    graph.append(tmp)

comb =combinations(chicken,m)
MIN=int(1e11)
for arr in list(comb):
    result=short_distance(house,arr)
    if MIN>result:
        MIN=result

print(MIN)