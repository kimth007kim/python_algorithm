# n,m=map(int,input().split())
# n,m=2,15
# coin=[2,3]
n,m=3,4
coin=[3,5,7]
# coin=[]
# for i in range(n):
#     coin.append(int(input()))
d=[10001]*(10001)
for j in coin:
    d[j]=1
v= min(coin)

# for i in range(v,m+1):
#     print(i)
#     for j in coin:
#         if d[i-j] !=0 :
#             d[i]=d[i-j]+1
for i in range(v,m+1):
    for j in coin:
        if d[i-j] !=10001 :
            d[i]=min(d[i],d[i-j]+1)
if d[m]==10001:
    print(-1)
else:
    print(d[m])