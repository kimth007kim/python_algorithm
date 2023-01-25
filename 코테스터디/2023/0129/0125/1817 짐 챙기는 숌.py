n, m = map(int, input().split())

if n==0:
    print(0)

else:
    arr = list(map(int, input().split()))

    tmp = 0
    answer = 0
    for i in range(n):
        if tmp+arr[i]<=m:
            tmp+=arr[i]
        else:
            tmp=arr[i]
            answer+=1

    if tmp>0:
        answer+=1

    print(answer)