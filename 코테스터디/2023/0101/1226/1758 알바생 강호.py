import sys

input =sys.stdin.readline


n= int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

# print(arr)
arr.sort()
total=0

for i in range(n,0,-1):
    # print(i, arr[i-1],n-i+1)
    tmp = arr[i-1]-(n-i)
    if tmp>0:
        total+=tmp

print(total)