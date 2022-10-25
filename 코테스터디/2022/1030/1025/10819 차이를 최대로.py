from itertools import permutations

def calc(t):
    global MAX
    total = 0
    for i in range(len(t) - 1):
        tmp = abs(arr[t[i]] - arr[t[i + 1]])
        total += tmp
    MAX = max(MAX, total)

MAX = 0

n=int(input())
arr =list(map(int,input().split()))
comb = permutations(range(n), n)
for i in list(comb):
    calc(i)
    # break
print(MAX)
