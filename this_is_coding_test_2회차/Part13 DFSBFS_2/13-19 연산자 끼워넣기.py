n= int(input())
number=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())
word=""
word+=str(number[0])
max_value=-1e9
min_value=1e9

def calc(cnt,word):
    global add,sub,mul,div,min_value,max_value
    if cnt==n:
        temp1=word[:1]
        temp2=word[1:]
        answer=""
        result=0
        for i in range(0,len(temp2)+1,2):
            # print(i)
            # print(temp1,"temp2[:i]=",temp2[:i])
            temp1+= temp2[i:i+2]
            result=int(eval(temp1))
            temp1=str(result)
        min_value=min(min_value,result)
        max_value=max(max_value,result)
        return

    if add>0:
        add-=1
        calc(cnt+1,word+"+"+str(number[cnt]))
        add+=1
    if sub>0:
        sub-=1
        calc(cnt+1,word+"-"+str(number[cnt]))
        sub+=1
    if mul>0:
        mul-=1
        calc(cnt+1,word+"*"+str(number[cnt]))
        mul+=1
    if div>0:
        div-=1
        calc(cnt+1,word+"/"+str(number[cnt]))
        div+=1



calc(1,word)
print(max_value)
print(min_value)
