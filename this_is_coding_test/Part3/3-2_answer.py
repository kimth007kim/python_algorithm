
cnt, m, k = map(int,input().split())
nlist = list(map(int,input().split()))
result=0
cnt=0

nlist.sort()
num1=nlist[cnt-1]
num2=nlist[cnt-2]

result = k*(m//k)*num1 + (m%k)*num2


print(result)


# 2 4 4 5 6
# M=8번 더해야하는데 최댓값 쓸수있는건 K=3번 뿐
# 6 6 6 5 이런식으로

# 0 1 2
# 4 5 6
# 3 7