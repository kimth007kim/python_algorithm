n= int(input())
m=list(map(int,input().split()))

cnt=0
m.sort()
while m:
    print(m)
    mim=m[0]
    for i in range(mim):
        del m[0]
    cnt+=1

print(cnt)