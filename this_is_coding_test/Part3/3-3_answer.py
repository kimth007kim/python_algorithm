n, m = map(int,input().split())

result=0
for i in range(n):
    data = list(map(int,input().split()))
    min_value=min(data)
    print("min_value",min_value)
    result =max(result,min_value)
    print("result:",result)
print(result)