n,m=map(int,input().split())
won= []
for _ in range(n):
    won.append(int(input()))

d=[10001]* (m+1)

d[0]=0
for i in range(n):
    for j in range(won[i],m+1):
        if d[j-won[i]]!= 10001:
            d[j]= min(d[j],d[j-won[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])