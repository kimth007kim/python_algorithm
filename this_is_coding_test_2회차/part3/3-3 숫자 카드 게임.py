n,m= map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

NUMBER=0
for j in range(n):
    if NUMBER < min(data[j]):
        NUMBER=min(data[j])
print(NUMBER)