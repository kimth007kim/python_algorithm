n=int(input())
space=[]
for i in range(n):
    d,s= map(str,input().split())
    s=int(s)
    space.append((d,s))

array =sorted(space ,key=lambda space:space[1])
print(array)