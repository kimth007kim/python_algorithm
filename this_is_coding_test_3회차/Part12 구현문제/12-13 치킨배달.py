from itertools import combinations
import sys

input =sys.stdin.readline

def calcABS(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def checkDistance(data):
    h=[]
    c=[]
    result=0
    for i in range(n):
        for j in range(n):
            if data[i][j]==1:
                h.append([i,j])
            elif data[i][j]==2:
                c.append([i,j])

    for hx,hy in h:
        MIN=int(1e9)
        for cx,cy in c:

            dist = calcABS(hx,cx)+calcABS(hy,cy)
            MIN=min(MIN,dist)
        result+=MIN
    return result


n,m = map(int,input().split())
data=[]
chicken=[]
answer=[]




for i in range(n):
    tmp= list(map(int,input().split()))
    for j in range(n):
        if tmp[j]==2:
            chicken.append((i,j))

    data.append(tmp)

for i in range(len(chicken)-m,len(chicken),1):
# for i in range(0,m):
    comb = combinations(chicken,i)
    for j in list(comb):
        d = data[:]
        for x,y in j:
            d[x][y]=0
        answer.append(checkDistance(d))
        for x,y in j:
            d[x][y]=2
    # print(list(comb))

print(min(answer))