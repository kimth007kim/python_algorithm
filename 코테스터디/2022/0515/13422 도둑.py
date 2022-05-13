def check(number,target):
    if number <target:
        return True
    return False

t= int(input())
answer=[]
for _ in range(t):
    n,m,k= map(int,input().split())

    arr=list(map(int,input().split()))
    cnt= 0
    arr+=arr[:m-1]
    now = sum(arr[:m])
    if check(now, k):
        cnt+=1
    if n==m:
        answer.append(cnt)
        continue
    prev= 0
    now -= arr[prev]

    for i in range(m,len(arr)):
        now+=arr[i]
        if check(now, k):
            cnt += 1
        prev+=1
        now-=arr[prev]
    # print(arr)
    answer.append(cnt)


for i in answer:
    print(i)