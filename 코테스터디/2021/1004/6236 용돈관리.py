# n일 동안 자신이 사용활 금액
# m 번만 통장에서 돈을 빼서 씀

n,m = map(int,input().split())
# daily = list(int(input()) for _ in range(n))
arr=[]
for i in range(n):
    arr.append(int(input()))
# print(daily)

start=min(arr)
end = sum(arr)

while start<=end:
    print(start,end)
    mid = (start+end)//2

    total=mid
    cnt=1
    print("시작전 mid: {} ,cnt: {}".format(mid, cnt))
    for i in arr:
        if total<i:
            cnt+=1
            total=mid
        total-=i
        print(total,cnt)
    print("-------실행후 mid: {} ,cnt: {}".format(mid,cnt))
    if cnt>m or mid<max(arr):
        start = mid+1
    else:
        end =mid-1
        k=mid

print(k)