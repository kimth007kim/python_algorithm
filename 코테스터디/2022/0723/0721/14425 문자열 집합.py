from collections import defaultdict
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
dict = defaultdict(int)
for i in range(n):
    word = input().rstrip()
    dict[word]=1
answer=0
for i in range(m):
    target = input().rstrip()
    # print(target)
    # print(dict[target])

    answer+=dict[target]

print(answer)