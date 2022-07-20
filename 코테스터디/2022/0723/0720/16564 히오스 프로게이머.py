n,m = map(int,input().split())

arr=[]
for i in range(n):
    a= int(input())
    arr.append(a)


arr.sort()
start=arr[0]
end= arr[n-1]+m
dist = arr[0]
while start<=end:
    mid = (start+end)//2
    # print(start,end,mid)
    remain=0
    for i in arr:
        if i>=mid:
            continue
        remain+=mid-i
    # break
    if remain<m:
        dist= max(dist,mid)
        start= mid+1
    elif remain==m:
        dist=mid
        break
    else:
        end=mid-1
print(dist)