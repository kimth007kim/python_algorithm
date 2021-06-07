n=int(input())
data= list(map(int,input().split()))

def binary_search(start,end,data):
    while start<=end:
        mid = (start+end)//2
        if data[mid] ==mid:
            return mid
        elif data[mid]<mid:
            start=mid+1
        else:
            end=mid-1
cnt=binary_search(0,n,data)

if cnt==None:
    print(-1)
else:
    print(cnt)