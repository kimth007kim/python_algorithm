n=int(input())
data=list(map(int,input().split()))

data.sort()

print(data)
result=1

for i in data:
    if i>result:
        break
    else:
        result+=i
        print(result)

print(result)