n= int(input())
data=[]
for i in range(n):
    data.append(int(input()))


data.sort()

result=data[0]
for i in range(1,n):
    if i!=1:
        result*=2
    result+=data[i]
print(result)