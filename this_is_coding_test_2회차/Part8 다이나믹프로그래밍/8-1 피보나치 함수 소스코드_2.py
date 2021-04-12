def fibo(num):
    if num==1 or num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

print(fibo(4))