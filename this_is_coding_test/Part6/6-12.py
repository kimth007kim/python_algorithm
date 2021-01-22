n,k= map(int,input().split())
a= list(map(int,input().split()))
b= list(map(int,input().split()))
cnt=0
a.sort()
b.sort(reverse=True)

print(a,b)
for i in range(k):
    if b[i]>a[i]:
        a[i]=b[i]

for j in a:
    cnt+=j

print(cnt)