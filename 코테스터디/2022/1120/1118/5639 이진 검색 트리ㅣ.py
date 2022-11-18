arr= list()
while True:
    num = input()
    if not num:
        break
    arr.append(int(num))

def postorder(first,end):
    if first>end:
        return
    mid = end+1
    for i in range(first+1,end+1):
        if arr[first]<arr[i]:
            mid =i
            break
    print("mid=",mid)
    print("first , end",first,end)

    postorder(first+1,mid-1)
    postorder(mid,end)
    print(arr[first])
postorder(0,len(arr)-1)