s="576"
arr=list(s)
result=0
for i in range(len(arr)):
    if arr[i]=="0" or result==0:
        result+=int(arr[i])
    else:
        result*=int(arr[i])

print(result)