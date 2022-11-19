def dfs(start,end):
    if start>end:
        return
    tmp=end+1
    for i in range(start+1,end+1):
        if arr[start]<arr[i]:
            tmp=i
            # print(arr[i],arr[start])
            break
    # print(tmp)
    dfs(start+1,tmp-1)
    dfs(tmp,end)
    print(arr[start])
arr=[]
# while True:
#     try:
#         n= int(input())
#         arr.append(n)
#         # print(n)
#     except:
#         break
arr=[50, 30, 24, 5, 28, 45, 98, 52, 60]
# print(arr)
dfs(0,len(arr)-1)


