n= int(input())
data=list(map(int,input().split()))

data.sort(reverse=True)
print(data)

index=n-1
result=0

while True:
    if len(data)<=0 or data[0]>len(data):
        print(result)
        break
    else:
        index = data[0]
        for i in range(index):
            data.pop(0)
        result+=1


