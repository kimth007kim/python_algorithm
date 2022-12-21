n=int(input())
arr= [1]*10

for i in range(n-1):
    for j in range(1,10):
        arr[j]+=arr[j-1]
print(sum(arr)%10007)