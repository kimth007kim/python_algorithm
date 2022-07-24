n,k = map(int,input().split())

play = list(map(int,input().split()))
mine = list(map(int,input().split()))

arr=[]
for i in range(n):
    MAX=-int(1e9)
    point=0
    for j in range(n):
        tmp=mine[i]*play[j]
        # print(tmp)
        if MAX<tmp:
            MAX=tmp
            point=play[j]
    arr.append([MAX,mine[i],point])


arr.sort(key =lambda x:(-x[0]))
# print(arr)
arr=arr[k:]
print(arr[0][0])