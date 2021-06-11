n=int(input())
t=[]
p=[]
d=[0]*(n+1)
max_value=0
for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    print(i,t[i])
    time =t[i]+i
    if time<=n:
        d[i]=max(p[i]+d[time],max_value)
        print(d)
        max_value=d[i]
    else:
        d[i]=max_value

print(max_value)