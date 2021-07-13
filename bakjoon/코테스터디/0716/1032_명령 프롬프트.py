# n= int(input())
# data=[]
# for i in range(n):
#     data.append(input())
n=3
data=["config.sys","config.inf","configures"]

cnt=0
for j in range(len(data[0])):
    for i in range(n):
        print(data[i][j])