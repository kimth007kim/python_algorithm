t = int(input())
ans=[]
for i in range(t):
    n= int(input())
    d=[0]*(n+1)
    d[1]=1
    d[2]=2
    d[3]=4
    for j in range(4,n+1):
        d[j]=d[j-1]+d[j-2]+d[j-3]
    ans.append(d[n])
for j in ans:
    print(j)