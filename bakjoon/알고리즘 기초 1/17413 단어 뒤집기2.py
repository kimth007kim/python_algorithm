import sys
input = sys.stdin.readline



data=list(input().strip())
result=[]
cnt=0
ccnt=0

answer=[]
tmp=[]


def reverse(tmp,answer):
    c=""
    for i in range(len(tmp)):
        answer.append(tmp.pop())


for i in range(len(data)):

    #마지막일떄 캐릭터면 삽입
    if i== len(data)-1:
        if data[i] != "<" and data[i] != ">" and data[i] != " " and cnt ==0 and ccnt == 1:
            tmp.append(data[i])
            reverse(tmp,answer)

    # 문자열이면 ccnt+=1
    if data[i] != "<" and data[i] != ">" and data[i] != " " and cnt==0 and ccnt==0:
        ccnt=1
    if data[i]=="<":
        cnt+=1
        if ccnt==1:
            reverse(tmp,answer)
            ccnt=0
    elif data[i]==">":
        cnt=0
    elif data[i]==" " and cnt !=1:
        if ccnt==1:
            reverse(tmp,answer)
            ccnt=0

    if ccnt==1:
        tmp.append(data[i])
    else:
        answer.append(data[i])


print("".join(answer))