d=[0]*30001

d[2]=1
x=int(input())

for i in range(3,x+1):
    d[i]=d[i-1]+1
    if i%5==0:
        d[i]=min(d[i],d[i//5]+1)
    if i%3==0:
        d[i]=min(d[i],d[i//3]+1)
    if i%2==0:
        d[i]=min(d[i],d[i//2]+1)


for i in range(1,x+1):
    print(i,d[i])