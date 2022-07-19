import sys
from  collections import defaultdict

input = sys.stdin.readline

n= int(input())
mosq = defaultdict(int)

for _ in range(n):
    x,y = map(int,input().split())
    mosq[x]+=1
    mosq[y]-=1

coors = list(mosq.keys())
coors.sort()

result= []
total=0

for i in coors:
    total+=mosq[i]
    result.append(total)

print(coors)
print(result)
max_num = max(result)

start =result.index(max_num)
end =start

while end< len(result) and result[end] == max_num:
    end+=1
    print("end=",end)

print(max_num)
print(coors[start],coors[end])