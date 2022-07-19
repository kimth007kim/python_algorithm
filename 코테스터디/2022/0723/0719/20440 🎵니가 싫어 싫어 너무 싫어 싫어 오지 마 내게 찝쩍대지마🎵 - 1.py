from collections import defaultdict
import sys

input =sys.stdin.readline
n= int(input())
time = defaultdict(int)
for i in range(n):
    a,b = map(int,input().split())
    time[a]+=1
    time[b]-=1

idx=[]
mosq=[]

for i in time:
    idx.append(i)
idx.sort()
prev=0
for i in idx:
    prev+=time[i]
    mosq.append(prev)
MAX=max(mosq)

start=0
find=0
end=0
for i in range(len(mosq)):
    if mosq[i]==MAX and find==0:
        start=i
        end=i
        find=1
    elif mosq[i]==MAX and find==1:
        end=i
    elif mosq[i]!=MAX and find==1:
        end=i
        break
print(MAX)
print(idx[start],idx[end])