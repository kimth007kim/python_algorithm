import sys

input =sys.stdin.readline

def dfs(a,b,c,idx,cnt):
    global mr,mg,mb
    # print(a,b,c,idx,cnt)
    if cnt>7:
        return
    if cnt>=2:
        tmp=abs(tr-mr)+abs(tg-mg)+abs(tb-mb)
        now=abs(tr-a//cnt)+abs(tg-b//cnt)+abs(tb-c//cnt)
        if tmp>now:
            mr,mg,mb= a//cnt,b//cnt,c//cnt
    for i in range(idx+1,n):
        a1,b1,c1= arr[i]
        dfs(a+a1,b+b1,c+c1,i,cnt+1)

arr=[]
n=int(input())
for i in range(n):
    x,y,z= map(int,input().split())
    arr.append([x,y,z])
tr,tg,tb= map(int,input().split())
mr,mg,mb=int(1e9),int(1e9),int(1e9)

for i in range(n):
    a,b,c = arr[i]
    dfs(a,b,c,i,1)

print(abs(tr-mr)+abs(tg-mg)+abs(tb-mb))
