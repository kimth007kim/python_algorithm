n= 4
array=[1,3,1,5]
# n= int(input())
# array=list(map(int,input().split()))
d=[0]*1000
d[0]=array[0]
d[1]=max(array[0],array[1])

for i in range(2,n):
    d[i]=max(d[i-2]+array[i],d[i-1])

print(d[n-1])