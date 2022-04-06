n,m= map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

for tmp in b:
    a.append(tmp)
a.sort()
print(*a)