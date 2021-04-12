d=[0]*101


n= int(input())
array= list(map(int,input().split()))


d[0]=array[0]
d[1]=max(array[0],array[1])

for i in range(2,n):
    print(d[i-1],array[i]+d[i-2])
    d[i]=max(d[i-1],array[i]+d[i-2])

print(d[n-1])