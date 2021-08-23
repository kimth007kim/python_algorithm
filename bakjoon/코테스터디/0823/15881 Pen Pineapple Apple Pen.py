n=int(input())
data= input()

idx=[]
cnt=0
if n <3:
    print(0)
else:
    for i in range(4,n+1):
        if i-3 in idx:
            continue
        else:
        # print(i-4,i)
        # print(data[(i-4):i])
            if data[i-4:i] =="pPAp":
                cnt+=1
                idx.append(i)
print(cnt)