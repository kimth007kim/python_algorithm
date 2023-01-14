from collections import defaultdict
import sys

input =sys.stdin.readline
n=int(input())
arr=[]
idx =set()
dic= defaultdict(set)
for i in range(n):
    tmp=input().rstrip()
    dic[len(tmp)].add(tmp)
    idx.add(len(tmp))

idx =list(idx)
idx.sort()
for i in idx:
    tmp=list(dic[i])
    tmp.sort()
    for j in tmp:
        print(j)
