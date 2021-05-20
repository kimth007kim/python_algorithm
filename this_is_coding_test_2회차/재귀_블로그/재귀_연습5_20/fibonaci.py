num=10
result=0
arr=[]
for i in range(num):
    if i==0:
        arr.append(0)
    elif i==1 or i ==2:
        arr.append(1)
    else:
        arr.append(arr[i-1]+arr[i-2])

print(arr)

fibo=[]
for i in range(6):
    fibo[i]=fibo[i-1]+fibo[i-2]

# def fibo(n):
#     print(n)
#     if n == 1 or n==2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
#
# print(fibo(6))