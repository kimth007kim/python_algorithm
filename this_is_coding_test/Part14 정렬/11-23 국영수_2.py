n=int(input())
array=[]
for i in range(n):
    a,b,c,d= map(str,input().split())
    array.append((a,b,c,d))


array.sort(key= lambda x : (-int(x[1]),int(x[2]), -int(x[3]),x[0]))

for j in array:
    print(j[0])