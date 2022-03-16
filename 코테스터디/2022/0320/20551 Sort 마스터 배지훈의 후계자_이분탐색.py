def binary_search(start,end,target,array):
    if start> end:
        return -1
    mid =(start+end)//2
    if array[mid]== target:
        if end == mid:
            return mid
        return binary_search(start, mid, target, array)
    elif array[mid]>target:
        return binary_search(start,mid-1,target,array)
    elif array[mid]<target:
        return binary_search(mid+1,end,target,array)
n , m = map(int,input().split())
array = [ int(input()) for _ in range(n)]
quiz=[int(input()) for _ in range(m)]
array.sort()
result =[]
MIN= array[0]
MAX = array[n-1]

for i in quiz:
    if MIN<=i<=MAX:
        result.append(binary_search(0,len(array),i,array))
    else:
        result.append(-1)

for i in result:
    print(i)