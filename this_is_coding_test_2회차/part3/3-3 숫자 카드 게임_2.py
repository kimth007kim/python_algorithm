n,m= map(int,input().split())

data=[]
small=0
for i in range(n):
    data.append(list(map(int,input().split())))
    if i ==0:
        small=min(data[i])
    else:
        small=max(small,min(data[i]))

print(small)