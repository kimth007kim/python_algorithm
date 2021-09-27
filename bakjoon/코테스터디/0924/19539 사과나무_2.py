n= int(input())
arr=  list(map(int,input().split()))

d=0
r= 0

for i in arr:
    d+=i //2
    r+=i %2
    print(d,r)

if (d-r )% 3==0 and d>=r:
    print("YES")
else:
    print("NO")