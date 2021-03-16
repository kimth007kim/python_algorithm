# n= 볼링공의 갯수
# m= 공의 최대 무게

n,m=map(int,input().split())
num=list(map(int,input().split()))

count =0
initNum=0

for i in range(len(num)):
    initNum= num[i]
    for j in range(len(num)):
        if initNum!=num[j]:
            # print(initNum, num[j])
            count+=1
            # print(count)
count= count//2
print(count)