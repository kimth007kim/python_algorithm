n=int(input())
data=list(map(int,input().split()))
data.sort()
print(data)

print((n-1)//2)
print(n//2)
print(data[(n-1)//2])