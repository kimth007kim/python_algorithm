
n= int(input())
dic= {}
result=0
for i in range(n):
    a,b= map(int,input().split())
    if a not in dic:
        dic[a]=b
    else:
        if b!=dic[a]:
            result+=1
            dic[a]=b

print(result)