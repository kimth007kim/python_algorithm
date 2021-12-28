import sys
input = sys.stdin.readline

n= int(input())
distance=list(map(int,input().split()))
gas=list(map(int,input().split()))
prev=gas[0]
total=0
answer=[0]
for i in range(1,len(gas)-1):
    if prev> gas[i]:
        prev= gas[i]
        answer.append(i)

answer.append(len(gas)-1)

result=0

for i in range(len(answer)-1):
    tmp=0
    for j in range(answer[i],answer[i+1]):
        tmp+=distance[j]
    result+= tmp*gas[answer[i]]
print(result)