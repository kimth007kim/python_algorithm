
cnt, m, k = map(int,input().split())
nlist = list(map(int,input().split()))
result=0
cnt=0

nlist.sort()
print(nlist)
# print(nlist[len(nlist)-1])

for i in range(m):
    if cnt == k:
        result+=nlist[len(nlist)-2]
        cnt=0
        # print(result)
    else:
        cnt+=1
        result+=nlist[len(nlist)-1]
        # print(result)
print(result)
# 2 4 4 5 6
# M=8번 더해야하는데 최댓값 쓸수있는건 K=3번 뿐
# 6 6 6 5 이런식으로

# 0 1 2
# 4 5 6
# 3 7
