



def obst(cnt,data):
    global find
    if cnt==3:
        print(data)
        print(check(data))
        if check(data) ==True:
            find=True
        return
    print()
    for i in range(n):
        for j in range(n):
            if data[i][j]=="X":
                data[i][j]="O"
                obst(cnt+1,data)
                data[i][j]="X"

def check(data):
    for tx,ty in teacher:
        print(tx,ty)
        if tx-1 >=0:
            nx=tx-1
            while nx>=0:
                if data[nx][ty]=="O":
                    return False
                if data[nx][ty] == "S":
                    return True
                nx-=1

        if tx+1 <n:
            nx=tx+1
            while nx<n:
                if data[nx][ty]=="O":
                    return False
                if data[nx][ty] == "S":
                    return True
                nx+=1


        if ty-1 >=0:
            ny=ty-1
            while ny>=0:
                if data[tx][ny]=="O":
                    return False
                if data[tx][ny] == "S":
                    return True
                ny-=1


        if ty+1 <n:
            ny=ty+1
            while ny<n:
                if data[tx][ny]=="O":
                    return False
                if data[tx][ny] == "S":
                    return True
                ny+=1
    return False

n= int(input())
data=[]
student=[]
teacher=[]
find=False
for i in range(n):
    temp=list(map(str,input().split()))
    data.append(temp)
    for j in range(n):
        if temp[j]=="S":
            student.append((i,j))
        if temp[j] == "T":
            teacher.append((i,j))


obst(0,data)

if find:
    print("yes")
else:
    print("no")