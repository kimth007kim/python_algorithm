n=int(input())
card=list(map(int,input().split()))
m=int(input())
cnt=list(map(int,input().split()))

dic={}
for n in card:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
result=[]
for i in cnt:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(0)

for j in result:
    print(j,end=' ')