import sys
input = sys.stdin.readline

from itertools import combinations

n,m= map(int,input().split())
guitars=set()

for _ in range(n):
    name,pos =input().split()
    bin_change=""
    for chr in pos:
        if chr=="Y":
            bin_change+="1"
        else:
            bin_change+="0"
    print(bin_change)
    guitars.add(int(bin_change,2))

guitars-={0}
print(guitars)
if not guitars:
    print(-1)
    exit()
max_cnt=0

for i in range(1,n+1):
    for combs in combinations(guitars,i):
        total=0
        for num in combs:
            print(list(combs))
            total |= num
        cnt=0
        for j in range(m):
            print(1<<j," ",total,"   ",j)
            if total&(1<<j):
                cnt+=1
                # print(total)
        if max_cnt<cnt:
            max_cnt =cnt
            max_guitar =i

print(max_guitar)