arr= [2,6, 1, 5, 4, 3]
length= len(arr)

for i in range(length):
    val=int(1e9)
    idx=i
    for j in range(i,length):
        if val>arr[j]:
            val=arr[j]
            idx=j
    arr[i],arr[idx]= arr[idx],arr[i]
    print(arr)
    # print(val,idx)