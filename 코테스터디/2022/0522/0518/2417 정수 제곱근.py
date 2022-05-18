def binary_search(start,end,target):
    global answer
    while start<=end:
        mid = (start+end)//2
        if target<=mid**2:
            end=mid-1
            answer=min(answer,mid)
        elif target>mid**2:
            start=mid+1

answer=1e15
arr=[]
n= int(input())
MAX=(2**32)
binary_search(0,MAX,n)
print(answer)