def binary_search(na,target,start,end):
    while start<= end:
        mid= (start+end)//2
        if na[mid]== target:
            return 1
        elif na[mid]>target:
            end= mid-1
        else:
            start= mid+1
    return 0


n= int(input())
na= list(map(int,input().split()))
na.sort()
m= int(input())
ma= list(map(int,input().split()))

for j in range(m):
    target= ma[j]
    print(binary_search(na,target,0,n-1))
