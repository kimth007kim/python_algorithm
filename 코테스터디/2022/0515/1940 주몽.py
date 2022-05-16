n= int(input())  #재료의 개수
m= int(input()) #갑옷에 만드는데 필요한 수
arr=list(map(int,input().split())) #재료들 의 고유한 수

arr.sort()
start=0
end=n-1
cnt=0
while start<end:
    _sum = arr[start]+arr[end]
    if _sum<m:
        start+=1
    if _sum>m:
        end-=1
    if _sum==m:
        cnt+=1
        start+=1

print(cnt)