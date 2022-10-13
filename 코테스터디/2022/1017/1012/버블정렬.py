arr= [2, 1, 5, 4, 3]
length = len(arr)


for i in range(length-1):
    for j in range(length-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)