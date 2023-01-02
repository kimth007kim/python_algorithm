n,m = map(int,input().split())
arr = list(map(int,input().split()))

r=[0]*m
for i in range(n):
    arr[i]+=arr[i-1]
    r[arr[i]%m]+=1

cnt= r[0]
print("초기",cnt)
print(r)
for i in r:
    print(i)
    cnt+=i*(i-1)//2
    print("cnt",cnt)