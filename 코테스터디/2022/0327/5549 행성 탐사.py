n,m = map(int,input().split())
k= int(input())
command=[]
graph= [list(input()) for _ in range(n)]
# for _ in range(k):
#     command.append(list(map(int,input().split())))

ice=[[0]*(m+1) for _ in range(n+1)]
jungle=[[0]*(m+1) for _ in range(n+1)]
ocean=[[0]*(m+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,m+1):
        now = graph[i-1][j-1]
        if now =="O":
            ocean[i][j]+=1
        if now =="J":
            jungle[i][j]+=1
        if now =="I":
            ice[i][j]+=1
        ocean[i][j]=ocean[i][j-1]+ocean[i-1][j]-ocean[i-1][j-1]+ocean[i][j]
        jungle[i][j]=jungle[i][j-1]+jungle[i-1][j]-jungle[i-1][j-1]+jungle[i][j]
        ice[i][j]=ice[i][j-1]+ice[i-1][j]-ice[i-1][j-1]+ice[i][j]


print("ice")
for i in ice:
    print(i)
print()
print("jungle")
for i in jungle:
    print(i)
print()
print("ocean")
for i in ocean:
    print(i)
print()
answer=[]
# for x1,y1,x2,y2 in command:
#     print(x1,y1,x2,y2)
#     print(jungle[x2-1][y2-1],jungle[x1-1][y1-1],"    ",ocean[x2-1][y2-1],ocean[x1-1][y1-1],"       ",ice[x2-1][y2-1],ice[x1-1][y1-1])

for _ in range(k):
    a,b,c,d = map(int,input().split())
    print(jungle[c][d] - jungle[c][b-1] - jungle[a-1][d] + jungle[a-1][b-1],end=' ')
    print(ocean[c][d] - ocean[c][b-1] - ocean[a-1][d] + ocean[a-1][b-1],end=' ')
    print(ice[c][d] - ice[c][b-1] - ice[a-1][d] + ice[a-1][b-1])