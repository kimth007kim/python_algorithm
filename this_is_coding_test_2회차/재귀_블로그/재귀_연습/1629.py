a,b,c=map(int,input().split())

result=1
def mul(result,a,b):
    if b==0:
        return result %c
    return mul(result*a,a,b-1)


tot=mul(result,a,b)
print(tot)