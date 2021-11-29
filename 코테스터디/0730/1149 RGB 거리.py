import sys
input = sys.stdin.readline

n= int(input())
# 집은 빨강 초록 파랑 중 하나의 색으로 칠해야한다. 각각의 집을 빨강 초록 파랑으로 칠하는 비용이 주어졌을때,
# 모든 집을 칠하는 비용은?

color=[]
for i in range(n):
    r,g,b=map(int,input().split())
    color.append((r,g,b))

past=-1

result=0

for i in range(n):
    MIN= int(1e9)
    for j in range(3):
        if j == past:
            continue
        if MIN>color[i][j]:
            MIN=color[i][j]
            index=j
    result+=MIN
    past=index

print(result)