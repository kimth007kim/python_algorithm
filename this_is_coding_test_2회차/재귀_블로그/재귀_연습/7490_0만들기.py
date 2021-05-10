# t=int(input())
# for i in range(t):
#     n=int(input())

end=3
sik="1"
sum=1
result=[]

def calc(start,end,sik,sum,ope):
    if start == end:
        if sum==0:
            result.append(sik)
            sik="1"
            return
    if ope==0:
        sum+=start
        sik=sik+"+"+str(start)
    if ope == 1:
        sum -= start
        sik = sik + "-" + str(start)
    calc(start+1,end,sik,sum,0)
    calc(start+1,end,sik,sum,1)


calc(1+1,end,sik,sum,0)
calc(1+1,end,sik,sum,1)

print(result)