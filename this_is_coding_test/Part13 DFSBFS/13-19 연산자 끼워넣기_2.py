n= int(input())
num= list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

min_value=1e9
max_value=-1e9

def calc(i,now):
    global min_value,max_value,add,sub,div,mul
    if i==n:
        min_value=min(min_value,now)
        max_value=max(max_value,now)
    else:
        if add>0:
            add-=1
            calc(i+1,now+num[i])
            add+=1
        if sub>0:
            sub-=1
            calc(i+1,now-num[i])
            sub+=1
        if mul>0:
            mul-=1
            calc(i+1,now*num[i])
            mul+=1
        if div>0:
            div-=1
            calc(i+1,now*num[i])
            div+=1


calc(1,num[0])

print(max_value,min_value)