# n= int(input())
# data=list(map(int,input().split()))
n=5
data=[3, 2, 1, 1, 9]
data.sort()

target=1
for i in data:
    if target<i:
        break
    target+=i
print(target)