d=[0]*81
d[1]=1
d[2]=1

n= int(input())
for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]

answer= 2*(d[n]+d[n-1])+2*d[n]
print(answer)