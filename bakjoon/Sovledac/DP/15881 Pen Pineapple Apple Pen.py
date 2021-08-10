
n=int(input())
data = input()
cnt=0
idx=[]
for i in range(len(data)):
    if data[i]=="p":
        if i>2:
            if data[i-1] =="A" and data[i-2] =="P" and data[i-3] =="p" and i-3 not in idx:
                cnt+=1
                idx.append(i)
print(cnt)