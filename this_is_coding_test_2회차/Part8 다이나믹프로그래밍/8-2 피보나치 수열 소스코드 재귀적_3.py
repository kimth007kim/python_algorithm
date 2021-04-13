d=[0]*101
x= int(input())
d[1]=1
d[2]=1
def fibo(x):
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(x))