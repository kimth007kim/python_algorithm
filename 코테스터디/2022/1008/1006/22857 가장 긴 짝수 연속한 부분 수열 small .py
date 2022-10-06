n,k = map(int,input().split())
arr= list(map(int,input().split()))


# print(arr)
odd=0
end=0
total=0
MAX=0
for start in range(n):
    # print("MAX",MAX,"start",start,"end",end)
    while end<n and odd<=k:
        if arr[end]%2==0:
            total+=1
        else:
            odd+=1
        end+=1
        MAX=max(MAX,total)
    # break
    #     print(start,end,odd,total,MAX)
    if arr[start]%2==0:
        total-=1
    else:
        odd-=1
print(MAX)