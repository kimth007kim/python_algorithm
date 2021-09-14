n= int(input())
data=list(map(int,input().split()))
cnt=0
command=0
for i in data:
    if i == command:
        cnt+=1
        command+=1
        if command==3:
            command=0
print(cnt)
