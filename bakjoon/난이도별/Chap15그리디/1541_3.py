import sys

sik = list(map(str,sys.stdin.readline().rstrip().split('-')))

result=0
if len(sik)==1:
    dd=list(map(int,sik[0].split('+')))
    for j in dd:
        result += j
else:
    for j in range(len(sik)):
        if j ==0:
            result+=int(sik[j])
        else:
            dd= list(map(int,sik[j].split('+')))
            for k in dd:
                result-=k

print(result)