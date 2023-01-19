import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    candy, n = map(int, input().split())
    box = []
    for i in range(n):
        a, b = map(int, input().split())
        box.append(a * b)
    box.sort(reverse=True)
    total=0
    cnt=0
    for i in range(len(box)):
        total+=box[i]
        cnt=i+1
        if total>=candy:
            break
    print(cnt)