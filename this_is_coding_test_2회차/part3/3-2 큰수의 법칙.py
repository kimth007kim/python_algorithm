n,m,k= map(int,input().split())
# n 배열의 크기 5
# m 더해지는 횟수 8
# k 최대로 더해질수있는 횟수 3


num= list(map(int,input().split()))

maxNum=max(num)
num.remove(maxNum)

second=max(num)
num.remove(second)

cnt=0
result=0
while cnt<m:
    for i in range(k):
        result+=maxNum
        cnt+=1
    result+=second
    cnt+=1

print(result)