arr = [7,5,9,4,3,1,6,0,4,8]
larr =len(arr)

for i in range(larr):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[min_index]>arr[j]:
            min_index=j
            print(min_index)
    arr[i],arr[min_index]=arr[min_index],arr[i]
    print(arr)

print(arr)