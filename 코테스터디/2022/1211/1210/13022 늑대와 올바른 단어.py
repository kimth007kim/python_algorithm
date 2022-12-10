def check(start,end,tmp):
    n=len(tmp)//4
    target = "w"*n + "o"*n +"l"*n+"f"*n
    if target==tmp:
        return True
    return False



word= input()
arr=[]
start=0
for  i in range(len(word)):
    if word[i]=="f":
        arr.append(i)

for end in arr:
    tmp=word[start:end+1]
    # print(tmp)
    if len(tmp)%4!=0:
        continue
    if check(start, end, tmp):
        start=end+1
if start==len(word):
    print(1)
else:
    print(0)