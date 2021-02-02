# 4:49 스타트 5:29 끝

def binary_search(array,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if array[mid]==target:
            return True
        elif array[mid]>target:
            end= mid-1
        else:
            start=mid+1
    return None

n= int(input())
narray= list(map(int,input().split()))
narray.sort()
m= int(input())
marray=list(map(int,input().split()))
d=[]


for j in range(m):
    target= marray[j]
    result = binary_search(narray,target,0,n-1)
    if result == True:
        d.append("yes")
    else:
        d.append("no")

for k in d:
    print(k)