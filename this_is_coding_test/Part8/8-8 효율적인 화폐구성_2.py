array=[]
n,m= map(int,input().split())
d=[10001]*(m+1)
for i in range(n):
    array.append(int(input()))


d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        # print("i,j",i,j)
        if d[j-array[i]]!=10001:
            # print("적합")
            d[j]= min(d[j],d[j-array[i]]+1)

print(d)
if d[m]== 10001:
    print(-1)
else:
    print(d[m])