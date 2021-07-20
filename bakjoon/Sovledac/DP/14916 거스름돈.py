coin=[2,5]
# n=13
n=int(input())

d=[0]*(100001)
d[2]=1
d[5]=1
for i in range(3,n+1):
    for c in coin:
        if i>=c:
            if d[i-c]!=0:
                # print(i - c)
                if d[i]==0:
                    d[i]=d[i-c]+1
                else:
                    d[i]=min(d[i],d[i-c]+1)

if d[n]==0:
    print(-1)
else:
    print(d[n])