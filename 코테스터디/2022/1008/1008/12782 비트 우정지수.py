from collections import Counter
import sys

input =sys.stdin.readline
t= int(input())

for i in range(t):
    a,b= input().rstrip().split()
    a,b = list(a),list(b)
    ca, cb = Counter(a),Counter(b)
    answer=0
    length=0
    # print(a,b)
    for i in range(len(a)):
        if a[i]== b[i]:
            ca[a[i]]-=1
            cb[b[i]]-=1
        else:
            length+=1
    MIN=min(ca["1"],ca["0"])
    answer+=MIN+(length-MIN*2)
    print(answer)