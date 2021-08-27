import sys

input = sys.stdin.readline



def check(x, y):
    global cnt
    # x축 확인 세로
    xdata={}
    ydata={}
    for i in range(len(data)):
        if data[i][y] not in xdata:
            xdata[data[i][y]]=1
        else:
            xdata[data[i][y]]= xdata[data[i][y]]+1
    # y축 확인 가로
    for j in range(len(data)):
        if data[x][j] not in ydata:
            ydata[data[x][j]]=1
        else:
            ydata[data[x][j]]+=1
    MX=0
    for i in xdata:
        if xdata[i]>MX:
            MX=xdata[i]
    for i in ydata:
        if ydata[i]>MX:
            MX=ydata[i]

    cnt =max(cnt,MX)

n= int(input())
data=[]
for i in range(n):
    data.append(list(input().strip()))

cnt=1
axis=[]
for i in range(n):
    tmp=[]
    for j in range(n):
        tmp.append(data[j][i])
    axis.append(tmp)


for i in range(n-1):
    for j in range(n):
        if data[i][j]!=data[i+1][j]:
            tm1=data[i+1][j]
            tm2=data[i][j]
            data[i][j]= tm1
            data[i+1][j]= tm2

            check(i, j)
            check(i+1, j)

            data[i][j]=tm2
            data[i+1][j]=tm1
for i in range(n):
    for j in range(n-1):
        if data[i][j+1]!= data[i][j]:
        # print(data[i][j],i,j,"  ",data[i][j+1],i,j+1)
            tm1 = data[i][j+1]
            tm2 = data[i][j]
            data[i][j] = tm1
            data[i][j+1] = tm2

            check(i, j+1)
            check(i, j)

            data[i][j] = tm2
            data[i][j+1] = tm1

    # print(isCalc)
print(cnt)