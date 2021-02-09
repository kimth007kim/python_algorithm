# 1905스타트 1945까지

n,m =map(int,input().split())
h=list(map(int,input().split()))
avg=0
start=0
end=max(h)

result=0
while start<=end:
    total=0
    mid=(start+end)//2
    for i in h:
        if i>mid:
            total+= i-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start =mid+1

print(result)