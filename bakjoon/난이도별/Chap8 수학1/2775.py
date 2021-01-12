# 4시 16분 시작 5시 18분까지 봤지만 틀림
# 5시 55분 시작 6시 10분완료
ans=[]
for _ in range (int(input())):
    k=int(input())
    n=int(input())

    data = [i for i in range(1, n + 1)]

    for t in range(k):
        for i in range(1,n):
            data[i]+= data[i-1]
    ans.append(data[-1])
for i in range(len(ans)):
    print(ans[i])