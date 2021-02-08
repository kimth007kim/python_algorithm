n = int(input())
array= list(map(int,input().split()))

d = [0]*101
d[0]=array[0]
d[1] =max(array[0],array[1])
for i in range(2,n):
    print("i=",i,"d[i-1]=",d[i-1],"d[i-2]+array[i]=",d[i-2]+array[i])
    d[i]=max(d[i-1],d[i-2]+array[i])
    print("d[i]로 결정",d[i])

print(d[n-1])
print(d)