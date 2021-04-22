n=int(input())
array=list(map(int,input().split()))

def binary(array,start,end):
    while start <=end:
        mid=(start+end)//2
        # print(mid)

        if array[mid]==mid:
            return mid
        elif array[mid]<mid:
            return binary(array,mid+1,end)
        else:
            return binary(array,start,mid-1)
    return None


result =binary(array, 0, n-1)

if result==None:
    print(-1)
else:
    print(result)