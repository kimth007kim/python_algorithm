a,b=map(int,input().split())
data=list(map(int,input().split()))
cnt=0

for i in range(a):
    for j in range(i+1,a):
        if data[i]!=data[j]:
            cnt+=1

print(cnt)
