import sys
input = sys.stdin.readline

n,limit= map(int,input().split())
d=[0]*(limit+1)
arr=[]
for i in range(n):
    w,v=map(int,input().split())
    d[w]= max(d[w],v)
    arr.append([w,v])


for i in range(1,limit+1):
    for a,b in arr:
        if i+a>limit:
            continue
        else:
            d[i+a] =max(d[i+a],d[i]+b)

MAXVALUE= max(d)
d[limit]=max(d[limit],MAXVALUE)

print(d[limit])