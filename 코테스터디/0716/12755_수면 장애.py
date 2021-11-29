import sys
input=sys.stdin.readline()
n=int(input)

a=""
cnt=0
number=1
while cnt<=n:
    a+=str(number)
    # print(a)
    cnt+=1
    number+=1
print(a)
print(len(a))

print(a[n-1])