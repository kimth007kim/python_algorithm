arr=[2,5,3,8,1]
# 1,2,3     0,2,4
# 1,2,5     0,1,4   x
# 2,3,5     0,1,2   x
# 1,3,5     1,2,4
# 1,2,8     0,3,4   x
# 1,2,5,3   0,1,2,4 x
k=3
t=11

cnt=0

def calc_hap(index,arr):
    hap=0
    for i in index:
        hap+=arr[i]
    print(index,hap)
    return hap
def dfs(cnt,index,arr):
    if cnt>=k-1:
        if calc_hap(index,arr)>t:
            return
        else:
            index.sort()
            copy_list = index.copy()
            result.append(copy_list)
        # result.append(data)
    if cnt == LEN-1:
        return


    for i in range(LEN):
        if i in index:
            continue
        else:
            index.append(i)
            dfs(cnt + 1, index,arr)
            index.pop()

LEN=len(arr)
result=[]

for i in range(LEN):
    dfs(0,[i],arr)

# 8for j in range(i + 1, len(arr)):

print(result)
print(list(set(map(tuple,result))))