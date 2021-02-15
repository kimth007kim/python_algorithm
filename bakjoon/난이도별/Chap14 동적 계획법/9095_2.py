t = int(input())

test=[]
for _ in range(t):
    test.append(int(input()))
m= max(test)

d=[0]*(m+1)
d[1]=1
d[2]=2
d[3]=4

for j in range(4,m+1):
    d[j]= d[j-1]+d[j-2]+d[j-3]

for k in test:
    print(d[k])