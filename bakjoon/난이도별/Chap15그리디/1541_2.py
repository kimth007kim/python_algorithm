import sys

number=(list(map(str,sys.stdin.readline().rstrip().split('-'))))
result=0
print(number)
dd=[]

for j in range(len(number)):
    if '+' in number[j]:
        dd=(list(map(int,number[j].split('+'))))
        for k in range(len(dd)):
            if j>0:
                result-=dd[k]
            else:
                result+=dd[k]
    else:
        if j > 0:
            result -= int(number[j])
        else:
            result += int(number[j])

print(result)