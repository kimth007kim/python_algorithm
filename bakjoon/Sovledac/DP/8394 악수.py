d = [0]*10000001
d[1]=1
d[2]=2
n= int(input())

for i in range(3,n+1):
    tmp = str(d[i-1]+d[i-2])
    d[i]= int(tmp[-1])

print(d[n])