s=input()
slen=len(s)
data=[]
for i in range(slen):
    data.append(int(s[i]))

result=data[0]
for i in range(1,slen):
    if data[i] ==0 or result==0:
        result+=data[i]
    else:
        result*=data[i]

print(result)