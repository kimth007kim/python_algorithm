n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

now = arr[-1]
cnt=0

for i in range(n-2,-1,-1):
    if now<=arr[i]:
        tmp = now-1
        cnt+=arr[i]-tmp
        now = tmp
    else:
        now = arr[i]
print(cnt)