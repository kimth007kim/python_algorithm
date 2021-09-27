def binary_search(start, end ,arr):
    target= 0
    while start<=end:
    # for _ in range(3):
        total=0
        mid = (start+end)//2
        for i in arr:
            total+= i//mid
        if total<= n:
            end= mid-1
        else:
            start=mid+1

        if n== total:
            target = max(target,mid)
        # print(start,mid,end, total)
    return target

# k,n=4,11
# arr=[802, 743, 457, 539]
# MAX_NUM= 802
k, n = map(int,input().split())
arr= []
MAX_NUM= -1
for i in range(k):
    tmp=int(input())
    arr.append(tmp)
    if MAX_NUM< tmp:
        MAX_NUM=tmp

answer= binary_search(1, MAX_NUM ,arr)
print(answer)

