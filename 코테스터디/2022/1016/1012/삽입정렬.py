arr= [2, 1, 5, 4, 3]
length= len(arr)
for i in range(len(arr)):
    for j in range(i):
        if arr[i]<arr[j]:
            print(i,j,"  ", arr[i],arr[j])
            arr[i],arr[j]=arr[j],arr[i]
            print(arr)
        # print(arr[i],arr[j])
    # print(i,arr[i])