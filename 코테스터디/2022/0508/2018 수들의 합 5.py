
n= int(input())

arr=  [i for i in range(1,n+1)]
start =0
end=0
prefix_sum=arr[0]
result=[]
cnt=0
while start<len(arr) and end<len(arr):
    if end >= len(arr) or start>= len(arr):
        break
    if prefix_sum==n:
        # print(arr[start:end+1])
        # result.append(arr[start:end+1])
        cnt+=1
        prefix_sum-=arr[start]
        start+=1

    elif prefix_sum<n:
        end+=1
        if end >= len(arr):
            break
        prefix_sum+=arr[end]
    else:
        prefix_sum-=arr[start]
        start+=1
print(cnt)