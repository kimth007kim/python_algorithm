a=input()

result= 1

for i in range(len(a)):

    pp=int(a[i])
    if pp==0 or pp==1:
        result+=int(a[i])
    else :
        result= result*int(a[i])

print(result)
