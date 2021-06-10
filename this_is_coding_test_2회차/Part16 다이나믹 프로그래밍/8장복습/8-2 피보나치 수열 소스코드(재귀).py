x=int(input())
d=[-1]*(x+1)

def fibo(x):
    if x == 1 or x==2:
        return 1
    if d[x]!=-1:
        return d[x]
    d[x] =fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(x))