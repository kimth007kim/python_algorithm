data=input()

cnt0=0
cnt1=0

string=data[0]
if data[0]=="1":
    cnt1+=1
else:
    cnt0+=1

for i in range(len(data)-1):
    if data[i]!=data[i+1]:
        if data[i]=="1":
            cnt0+=1
        else:
            cnt1+=1


print(cnt0,cnt1)