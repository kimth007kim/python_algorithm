import sys

input = sys.stdin.readline
n,a,d = map(int,input().split())
arr= list(map(int,input().split()))

cnt=0
now_target=a
for i in range(n):
    if cnt==0 and arr[i]==now_target:
        cnt=1
        now_target+=d
    else:
        if arr[i]== now_target:
            cnt+=1
            now_target+=d

print(cnt)