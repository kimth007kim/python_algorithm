
a= int(input())
def fibo(a):
    if a<=0:
        return 1
    return a* fibo(a-1)

print(fibo(a))
