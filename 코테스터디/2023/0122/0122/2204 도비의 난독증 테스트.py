import sys

input = sys.stdin.readline

while True:
    t = int(input())
    if t==0:
        break
    arr=[]
    for i in range(t):
        tmp= input().rstrip()
        s=tmp.lower()
        arr.append([s,tmp])

    # print(arr)
    arr.sort(key = lambda x:x[0])
    # print(arr)
    print(arr[0][1])