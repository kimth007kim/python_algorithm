num=["0","1","2","3","4","5","6","7","8","9"]
result=""
answer=[]
def comb(cnt,result,num):
    if cnt ==4:
        answer.append(result)
        return
    for i in range(len(num)):
        fn= num.pop(i)
        comb(cnt+1,result+fn,num)
        num.append(fn)
        num.sort()

comb(0,result,num)

print(answer)