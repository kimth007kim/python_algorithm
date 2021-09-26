import sys

input = sys.stdin.readline


def binary_search(data,start,end):
    mid = (start+ end)//2
    total=0
    while total!=n:
        total = 0
        for i in data:
            total += i // mid
        if total == n:
            return mid
        elif total<n:
            mid-=1
        elif total>n:
            mid+=1

k,n= map(int,input().split())
data = []
cnt=0

for i in range(k):
    tmp = int(input())
    data.append(tmp)
    cnt+=tmp
start ,end= 1, max(data)
print(binary_search(data,cnt//n,data[-1]))

