# 4시 42분 시작

n= int(input())
narray= list(map(int,input().split()))
m= int(input())
marray=list(map(int,input().split()))

for j in range(m):
    target= marray[j]
    if target in narray:
        print("yes")
    else:
        print("no")
    # print(target)




# print("n,narray:",n,narray)
# print("m,marray:",m,marray)