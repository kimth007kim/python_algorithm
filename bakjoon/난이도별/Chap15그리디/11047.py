n,k = map(int,input().split())
coin=[]
cnt=0
for _ in range(n):
    coin.append(int(input()))

for j in range(len(coin)-1,-1,-1):
    if coin[j]<=k:
        cnt+=k//coin[j]
        k %= coin[j]

print(cnt)
