def sol(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    return sol(n-1)+sol(n-2)+sol(n-3)

for i in range(int(input())):
    print(sol(int(input())))