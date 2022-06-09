n,m= map(int,input().split())
arr= [ ]
for i in range(n):
    tmp = int(input())
    arr.append(tmp)


def binary_search(start,end):
    MAX=0
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for i in arr:
            cnt += i//mid
        if cnt>=m:
            MAX=max(MAX,mid)
            start=mid+1
        else:
            end=mid-1
        # print(mid)
    return MAX


print(sum(arr)-((binary_search(1,max(arr)))*m))
