d=[0]*101
x=int(input())

def fibo(x):
    print('f('+str(x)+')',end=' ')
    if x==1 or x==2:
        return 1
    d[x]= fibo(x-1)+fibo(x-2)
    return d[x]

fibo(6)