num = int(input())
long = input()
result=0
k = len(long)
if num == k:
    for i in range(k):
        result = result + int(long[i])

print(result)
