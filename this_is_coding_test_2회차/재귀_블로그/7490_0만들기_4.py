t=int(input())
result=[]
def solution(arr,idx,st,st2):
    if len(arr)-1 == idx:
        st+=str(arr[idx])
        st2+=str(arr[idx])
        n= int(eval(st))
        if n ==0:
            result.append(st2)
    else:
        solution(arr,idx+1,st+str(arr[idx]),st2+str(arr[idx])+" ")
        solution(arr, idx + 1, st + str(arr[idx])+"+", st2 + str(arr[idx]) +"+")
        solution(arr, idx + 1, st + str(arr[idx])+"-", st2 + str(arr[idx]) +"-")


for i in range(t):
    n=int(input())
    arr=[]

    for j in range(n):
        arr.append(j+1)
    solution(arr,0,"","")
    for k in result:
        print(k)
    result.clear()