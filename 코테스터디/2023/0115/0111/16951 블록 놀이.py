import sys

input =sys.stdin.readline


n, k = map(int,input().split())
arr =list(map(int,input().split()))
INF =int(1e15)
answer= INF
def check(i):
    tmp = [0] * (n)
    tmp[i] = arr[i]
    total=0
    for j in range(i - 1, -1, -1):
        now = tmp[j + 1] - k
        if now <1:
            return INF
        tmp[j]=now
    for j in range(i+1,n):
        tmp[j]=tmp[j-1]+k
    for j in range(n):
        if arr[j]!=tmp[j]:
            total+=1
    return total

for i in range(n):
    answer=min(answer,check(i))
print(answer)