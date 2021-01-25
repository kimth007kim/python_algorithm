import sys

storage=[]
n= int(sys.stdin.readline())
for i in range(n):
    storage.append(int(sys.stdin.readline()))

max_num= max(storage)
count=[0]*max_num
for j in range(len(storage)):
    count[storage[j]-1]+=1

for e in range(max_num):
    for d in range(count[e]):
        print(e+1)

