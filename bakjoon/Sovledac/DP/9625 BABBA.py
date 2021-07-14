import sys
input=sys.stdin.readline
a=1
b=0
n= int(input())
cnt=0
while n>cnt:
    na=a
    nb=b
    if a>0:
        na-=1*a
        nb+=1*a
    if b>0:
        na+=1*b
    # print("na,nb",na,nb)
    a=na
    b=nb
    cnt+=1
print(a,b)