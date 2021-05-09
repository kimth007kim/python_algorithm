t=int(input())
ans=[]
def solution(arr,idx,st,st2):
    if idx==(len(arr)-1):
        st+=str(arr[idx])
        st2+=str(arr[idx])
        n=int(eval(st))
        if n==0:
            ans.append(st2)

    else:
        print(st,st2)
        solution(arr,idx+1,st+str(arr[idx]),st2+str(arr[idx])+" ")
        solution(arr,idx+1,st+str(arr[idx])+"+",st2+str(arr[idx])+"+")
        solution(arr,idx+1,st+str(arr[idx])+"-",st2+str(arr[idx])+"-")

for i in range(t):
    n=int(input())
    arr=[]
    for j in range(n):
        arr.append(j+1)
        print(arr)
    solution(arr,0,"","")
    for i in ans:
        print(i)
    print()
    ans.clear()
