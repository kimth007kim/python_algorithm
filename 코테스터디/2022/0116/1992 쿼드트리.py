n= int(input())

graph = []
for i in range(n):
    graph.append(list(input()))


def recursion(x,y,n):
    check=graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                print("(", end="")
                recursion(x,y,n//2)
                recursion(x,y+n //2,n//2)
                recursion(x+n//2,y,n//2)
                recursion(x+n //2,y+n //2,n//2)
                print(")",end="")
                return
    print(check,end="")
recursion(0,0,n)