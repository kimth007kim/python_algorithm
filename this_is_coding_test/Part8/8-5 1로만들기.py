x=int(input())
cnt=0
while x!=1 and x>0:
    if x %5==0:
        x= x//5
        cnt+=1
        print(x)
        continue
    if x %3 ==0:
        x= x//3
        cnt+=1
        print(x)
        continue
    if x %2 ==0:
        x = x//2
        cnt+=1
        print(x)
        continue
    x=x-1
    cnt+1

print(cnt)