def factorial(n):
    if n<=0:
        return 1
    return n*factorial(n-1)

if __name__ == "__main__":
    for i in range(1,6):
        for i in range(1,6):
            print(factorial(i))