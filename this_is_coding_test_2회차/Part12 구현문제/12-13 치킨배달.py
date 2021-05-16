from itertools import combinations

def checking(hx,hy,sx,sy):
    answer= abs(hx-sx)+abs(hy-sy)
    return answer


n,m= map(int,input().split())
data=[]
house=[]
chicken=[]
for i in range(n):
    data.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            house.append((i,j))
        if data[i][j]==2:
            chicken.append((i,j))


newchicken=list(combinations(chicken,m))

array=[]
for i in range(len(newchicken)):
    result = 0
    for home in house:
        hx, hy = home
        answer=1e9
        for j in newchicken[i]:
            sx,sy=j
            answer=min(answer,checking(hx,hy,sx,sy))
        result+=answer
    array.append(result)

print(min(array))
