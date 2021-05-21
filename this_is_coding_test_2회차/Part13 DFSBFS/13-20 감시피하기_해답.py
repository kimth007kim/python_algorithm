



def obst(cnt,data):
    if cnt==3:
        temp=[]
        for x,y in teacher:
            for i in range(4):
                if check(x,y,i):
                    temp.append(1)
                else:
                    temp.append(0)
        find.append(temp)
        return
    for i in range(n):
        for j in range(n):
            if data[i][j]=="X":
                data[i][j]="O"
                obst(cnt+1,data)
                data[i][j]="X"

def check(x,y,direction):
    if direction==0:
        while x>=0:
            if data[x][y]=="O":
                return False
            if data[x][y] == "S":
                return True
            x-=1

    if direction==1:
        while x<n:
            if data[x][y]=="O":
                return False
            if data[x][y] == "S":
                return True
            x+=1


    if direction==2:
        while y>=0:
            if data[x][y]=="O":
                return False
            if data[x][y] == "S":
                return True
            y-=1

    if direction == 3:
        while y<n:
            if data[x][y]=="O":
                return False
            if data[x][y] == "S":
                return True
            y+=1
    return False

n= int(input())
data=[]
student=[]
teacher=[]
find=[]
isfind=False

for i in range(n):
    temp=list(map(str,input().split()))
    data.append(temp)
    for j in range(n):
        if temp[j]=="S":
            student.append((i,j))
        if temp[j] == "T":
            teacher.append((i,j))


obst(0,data)

for i in find:
    if 1 not in i:
        isfind=True



if isfind:
    print("YES")
else:
    print("NO")