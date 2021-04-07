target=int(input())
array=[1,3,5,7,9,11,13,15,17,19]
n=len(array)

def binary_search(target,start,end):
    while start<=end:
        mid = (start+end)//2
        print(mid)
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end = mid - 1
            print("end",end)
        else:
            start=mid+1
            print("start",start)


    return None

result = binary_search(target,0,n-1)
if result==None:
    print("없다.")
else:
    print(result)