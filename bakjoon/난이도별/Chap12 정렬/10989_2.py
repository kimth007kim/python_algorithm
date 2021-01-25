import sys

check_list=[0]*10001
n= int(sys.stdin.readline())
for i in range(n):
    d=int(sys.stdin.readline())
    check_list[d]+=1

for j in range(10001):
    if check_list[j] != 0:
        for k in range(check_list[j]):
            print(j)