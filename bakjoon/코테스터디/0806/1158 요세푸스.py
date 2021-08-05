n,k = map(int,input().split())

result=[]

word=""
cnt=0
c=0
tmp= [i for i in range(1,n+1)]
while len(tmp)>0:
    if c >= len(tmp):
        c=0
    cnt+=1
    a=tmp[c]
    c+=1

    if cnt == k:
        if c==len(tmp):
            c=0
        else:
            c-=1
        cnt=0
        tmp.remove(a)
        result.append(a)

answer="<"
for i in range(len(result)):
    answer+=str(result[i])
    if i!=len(result)-1:
        answer+=", "

answer+=">"
print(answer)