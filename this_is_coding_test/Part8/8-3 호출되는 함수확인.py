d=[0]*100

def pibo(x):
    print('f('+str(x)+')',end=' ')
    if x ==1 or x ==2:
        return 1
    if d[x] !=0:
        return d[x]
    d[x]=pibo(x-1)+pibo(x-2)
    return d[x]
pibo(6)

# def fibo(x):
#     print('f('+str(x)+')',end=' ')
#     if x==1 or x==2:
#         return 1
#     return fibo(x-1) + fibo(x-2)
# fibo(6)