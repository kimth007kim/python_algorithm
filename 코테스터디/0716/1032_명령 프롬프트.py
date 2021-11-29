import sys
input=sys.stdin.readline

# n= int(input())
# data=[]
# for i in range(n):
#     data.append(input())
n=3
data=["config.sys","config.inf","configures"]

result=""
for j in range(len(data[0])):
    cnt = 0
    for i in range(n):
        if i==0:
            tmp=data[i][j]
        else:
            if data[i][j]==tmp:
                cnt+=1
            else:
                break
    if cnt==n-1:
        result+=(data[i][j])
    else:
        result+="?"
print(result)