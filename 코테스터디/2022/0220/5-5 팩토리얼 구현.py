
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result =1
    for i in range(1,n+1):
        result*=i
    return result


# 재귀로 구현
def factorial_recursive(n):
    if n==0:
        return 1
    return n* factorial_recursive(n-1)

print( factorial_recursive(5))
print(factorial_iterative(5))