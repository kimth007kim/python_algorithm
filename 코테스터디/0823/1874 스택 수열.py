n= int(input())
cnt=1
data=[]
stack=[cnt]
answer=["+"]
for i in range(n):
    data.append(int(input()))

isFalse= True

for i in range(len(data)):
    print(data[i])
    while (len(stack)>0 and stack[len(stack)-1]<data[i]) or len(stack)==0:
        cnt += 1
        stack.append(cnt)
        answer.append("+")
    if stack[len(stack)-1]==data[i]:
        stack.pop(len(stack)-1)
        answer.append("-")
    elif stack[len(stack)-1]>data[i]:
        isFalse=False
    # if i > len(data) and stack[len(stack)-1]!=data[i+1]:
    #     isFalse= False
    print(answer,stack,cnt)
#
#
# print(answer,isFalse)
if not isFalse:
    print("NO")
else:
    for i in answer:
        print(i)