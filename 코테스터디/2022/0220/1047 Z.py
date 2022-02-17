# n,c,r = map(int,input().split())
# n,c,r=3,7,7
n,r,c=3,4,6
# graph= [[0]*2**n for _ in range(2**n)]
# print(graph)

def sol(n,r,c):
    if n==0:
        return 0
    print((n,r,c))

    return 2*(r%2)+(c%2) + 4*sol(n-1,int(r/2),int(c/2))


print(sol(n,r,c))