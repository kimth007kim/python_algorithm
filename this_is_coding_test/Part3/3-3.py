n, m = map(int,input().split())
nlist=[]
for i in range(n):
    data = list(map(int,input().split()))
    data.sort()
    nlist.append(data[0])
nlist.sort()
print(nlist[n-1])