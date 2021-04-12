n,m=map(int,input().split())
array=[]
for i in range(n):
    array.append(int(input()))

d=[10001]*10001
# n,m=2,15
# array=[2,3]

d[0]=0

for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] !=10001:
            d[j]=min(d[j-array[i]]+1,d[j])

# for j in range(m+1):
#     print(j,d[j])

if d[m]==10001:
    print(-1)
else:
    print(d[m])