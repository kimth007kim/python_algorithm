# https://www.acmicpc.net/problem/20364
import sys
from collections import defaultdict,deque

input =sys.stdin.readline

def find_way(target):
    now=target
    way =deque()
    way.appendleft(now)
    while now//2>=1:
        now = now//2
        way.appendleft(now)
    for i in way:
        if visited[i]==True:
            return i
    visited[target]=True
    return 0

n,q=  map(int,input().split())

visited=[False]*(n+1)
for i in range(q):
    target = int(input())
    print(find_way(target))
