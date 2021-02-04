def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]== target:
            return target
        elif array[mid]>target:
            end= mid-1
        else:
            start=mid+1
    return 0

n= int(input())
card=list(map(int,input().split()))
m= int(input())
cnt=list(map(int,input().split()))
card.sort()
dd=[]
for j in range(m):
    target=cnt[j]
    dd.append(binary_search(card,target,0,n-1))

for k in range(m):
    if dd[k] !=0:
        # print(dd[k])
        dd[k]=card.count(dd[k])

for i in dd:
    print(i,end=" ")
    # print(binary_search(card,target,0,n-1),end=" ")
# 방법1