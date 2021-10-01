import sys
input  = sys.stdin.readline

n,m = map(int,input().split())

data=[]
for i in range(n):
    data.append(list(map(int,input().split())))


prefix_sum=[[0]*(m+1) for _ in range(n+1)]
ps=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    value=0
    for j in range(1,n+1):
        value+=data[i-1][j-1]
        prefix_sum[i][j]=value

for i in range(1,n+1):
    value = 0
    for j in range(1,n+1):
        value+=prefix_sum[j][i]
        ps[j][i]=value


for k in ps:
    print(k)

answer=[]
command = int(input())
for _ in range(command):
    x1,y1,x2,y2=map(int,input().split())
    print("x1,y1,x2,y2",x1,y1,x2,y2)
    print("ps[x2][y2]",ps[x2][y2])
    tmp = ps[x2][y2]
    if y1!=1 and x1==1:
        a=1
    elif x1!=1  and y1==1:
        tmp -= ps[1][y2]
    print(tmp)

    print("-------------------")

    # total=0
    # for i in range(x1,x2+1):
    #     if y1==1:
    #         total+=prefix_sum[i][y2]
    #     else:
    #         total+= prefix_sum[i][y2]-prefix_sum[i][y1-1]
    # answer.append(total)









#
# for i in answer:
#     print(i)