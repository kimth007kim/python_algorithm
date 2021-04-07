target=int(input())
array=[1,3,5,7,9,11,13,15,17,19]
n=len(array)

def binary_search(array,target,start,end):
    print(start,end)
    if start>end:
        return None
    mid = (start+end)//2
    print("array[mid]",array[mid],mid)

    if array[mid]==target:
        return mid
    elif array[mid]> target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

result = binary_search(array,target,0,n-1)
if result==None:
    print("없다.")
else:
    print(result)