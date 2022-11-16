import sys

from collections import defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

dic = defaultdict(int)
MAX=0
length=0
end=0
for start in range(n):
    while end<n:
        if dic[arr[end]]+1>k:
            break
        dic[arr[end]]+=1
        end+=1
    MAX= max(MAX,end-start)
    dic[arr[start]]-=1
print(MAX)