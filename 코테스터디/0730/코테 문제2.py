arr=[2,5,3,8,1]
k=3
t=11

# arr=[1,1,2,2]
# k=2
# t=3

#
# arr=[1,2,3,2]
# k=2
# t=2


cnt=0

result=[]
def total(arr,index):
    tot= 0
    for i in index:
        tot+= arr[i]
    return tot

def dfs(cnt,index):
    if cnt==len(arr):
        return
    if cnt >= k-1:
        v=total(arr,index)

        if v<=t:
            a=index.copy()
            result.append(a)


    for i in range(len(arr)):
        if i not in index:
            index.append(i)
            dfs(cnt+1,index)
            index.pop()

for i in range(len(arr)):
    dfs(0,[i])

print(result)
for i in result:
    i.sort()
a=list(set(map(tuple,result)))
print(len(a))