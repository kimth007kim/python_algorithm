def factorial(now):
    if now==1:
        return now
    return now *factorial(now-1)

n,m = map(int,input().split())

print(factorial(n)//(factorial(m)*factorial(n-m)))

# print(result//6)