n = int(input())
number=list(map(int,input().split()))
oper=list(map(int,input().split()))
soper=["+","-","*","/"]
result=""
MAX=int(-1e9)
MIN=int(1e9)
result+=str(number[0])

def calc(cnt,oper,result):
    global MAX,MIN
    if cnt==n-1:
        arr=list(result)
        temp=""

        index=0
        for i in range(len(arr)):
            if ord(result[i])>=48 or ord(result[i])<=57:
                temp+=result[i]
                index+=1
                if index==3:
                    answer=int(eval(temp))
                    temp=str(answer)
                    index=1
            else:
                temp+=result[i]
                index+=1

        MAX=max(answer,MAX)
        MIN=min(answer,MIN)
        return

    for i in range(4):
        if oper[i]!=0:
            oper[i]-=1
            calc(cnt+1,oper,result+soper[i]+str(number[cnt+1]))
            oper[i]+=1


calc(0,oper,result)
print(MAX)
print(MIN)