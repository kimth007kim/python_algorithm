import sys
sys.setrecursionlimit(10**8)

n=int(input())
graph=[]
copy=[]
for i in range(n):
    temp=list(map(str, input().split()))
    graph.append(temp)
    copy.append(temp)

student=[]
teacher=[]
empty=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]=='S':
            student.append((i,j))
        if graph[i][j]=='T':
            teacher.append((i,j))
        if graph[i][j]=='X':
            empty.append((i,j))

print(teacher,student)
def check(student,cnt ):
    print()

def make_block(graph,cnt,x,y):
    if cnt == 3:
       return check(graph)

    for j in range(y,n):
        if graph[x][j]=='X':
            graph[x][j] == 'O'
            print(graph)
            if make_block(graph,cnt-1,x,j):
                return True
            graph[x][j]=='X'
    for i in range(x,n):
        for j in range(n):
            if graph[x][j] == 'X':
                graph[x][j] == 'O'
                print(graph)
                if make_block(graph,cnt-1,i,j):
                    return True
                graph[i][j]='X'
    return False

    print(cnt)
    for i in range(n):
        for j in range(n):
            # if cnt==3:
            #     for k in copy:
            #         print(k)
            #     print()
            #     copy=graph
            #     cnt=0
            if copy[i][j] =='X':
                copy[i][j]='O'
                make_block(cnt+1,copy,graph)


make_block(graph,0,0,0)