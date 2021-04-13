d=[0]*101

d[1],d[2]=1,1

x=int(input())

for i in range(3,x+1):
    d[i]=d[i-1]+d[i-2]
    print('f('+str(i)+') = '+str(d[i]))