def permutation(arr,start):
    print("함수 호출됨")
    print("arr={} start={}".format(arr,start))
    if len(arr)-1 ==start:
        print("---------------",arr)
        return

    for i in range(start,len(arr)):
        arr[start],arr[i]=arr[i],arr[start]
        print("arr={}  start: arr[{}]= {} idx: arr[{}] = {} ".format(arr,start, arr[start],i,arr[i]))
        permutation(arr,start+1)
        arr[i], arr[start]=arr[start],arr[i]

if __name__ =="__main__":
    arr=[1,2,3]
    permutation(arr,0)