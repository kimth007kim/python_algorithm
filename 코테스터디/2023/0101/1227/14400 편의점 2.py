import sys

input =sys.stdin.readline
n = int(input())

x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

midX=x[n//2]
midY=y[n//2]

total=0
for i in range(n):
    total+= abs(x[i]-midX)+abs(y[i]-midY)

print(total)