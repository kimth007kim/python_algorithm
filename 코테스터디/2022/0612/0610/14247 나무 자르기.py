n = int(input())

arr1= list(map(int,input().split()))
arr2= list(map(int,input().split()))

arr = []
for i in range(n):
    arr.append([arr2[i],arr1[i]])

arr.sort(reverse=True)
result =0
for i in range(n):
    a,b = arr[i][0],arr[i][1]

    result+=a*(n-1-i)+b
print(result)