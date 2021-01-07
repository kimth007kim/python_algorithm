n,m = map(int,input().split())
# n,m=17,4
cnt=0

while n!=1:
    if n %m==0:
        cnt+= 1
        n= n//m
    else:
        n -=1
        cnt+=1
print(cnt)
