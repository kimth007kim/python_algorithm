import sys

input = sys.stdin.readline

n= int(input())

graph= [[0]*n for _ in range(n)]
friends={}

dx= [-1,0,0,1]
dy=[0,-1,1,0]

def blank(x,y):
    cnt=0
    for i in range(4):
        nx= dx[i]+x
        ny= dy[i]+y
        if 0<= nx < n and 0<=ny<n and graph[nx][ny]==0:
            cnt+=1
    return cnt


def find(graph,friends,target):
    # print("target은 ", target, "입니다.")
    # print("좋아하는 친구들은 각각" ,friends[target])

    # 친구 목록을 리스트로 일단 저장
    fList =[]
    for i in friends[target]:
        if numberList[i].isSelected:
            fList.append(i)
    if len(fList)==0:
        MAX=-1
        for i in range(n):
            for j in range(n):
                if graph[i][j]!=0:
                    continue
                cnt=blank(i,j)
                if cnt>MAX:
                    MAX=cnt
                    tx=i
                    ty=j

        graph[tx][ty]= target
        numberList[target].isSelected=True
        numberList[target].x=tx
        numberList[target].y=ty

    else:
        copygraph=[[0]*n for _ in range(n)]
        cMAX=0
        # print("좋아하는 친구가 배치되어있군요")
        point=[]
        for i in fList:
            for j in range(4):
                nx = dx[j] + numberList[i].x
                ny = dy[j] + numberList[i].y
                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]==0:
                    copygraph[nx][ny]+=1
                    if cMAX<copygraph[nx][ny]:
                        cMAX=copygraph[nx][ny]
        # print("copygraph는!!")
        # for k in copygraph:
        #     print(k)
        if cMAX!=0:
            for i in range(n):
                for j in range(n):
                    if copygraph[i][j]==cMAX:
                        point.append([i,j])
                        # print(point)

            arr=[]
            for x,y in point:
                cnt=blank(x, y)
                # print("빈칸의 갯수는",x,y,cnt)
                arr.append([x,y,cnt])
            # print("arr의 길이는",len(arr),arr)
            if len(arr)>=1:
                arr.sort(key = lambda x:(-x[2],x[0],x[1]))
                # print(arr[0][0],arr[0][1])
                graph[arr[0][0]][arr[0][1]] = target
                numberList[target].isSelected = True
                numberList[target].x = arr[0][0]
                numberList[target].y =arr[0][1]
        else:
            for i in range(n):
                for j in range(n):
                    if graph[i][j]==0:
                        graph[i][j]=target
                        numberList[target].isSelected = True
                        numberList[target].x = i
                        numberList[target].y = j

class Student:
    def __init__(self,id):
        self.id= id
        self.isSelected=False
        self.x=None
        self.y=None
    def __str__(self):
        return "id :{} , 선택됨: {}".format(self.id,self.isSelected)

numberList=[]
for i in range(n*n+1):
    numberList.append(Student(i))

for i in range(n*n):
    target,f1,f2,f3,f4=map(int,input().split())
    tmp=[f1,f2,f3,f4]
    friends[target]=tmp
    # print(target,tmp,graph)
    find(graph,friends,target)

# for i in graph:
#     print(i)


score=0
print(friends)
for i in range(n):
    for j in range(n):
        seq=0
        now = graph[i][j]
        for k in range(4):
            nx= dx[k]+i
            ny= dy[k]+j
            if 0<= nx <n and 0<=ny<n:
                # print(nx,ny,graph[nx][ny])
                if graph[nx][ny] in friends[now]:
                    seq+=1
        if seq==4:
            score+=1000
        elif seq==3:
            score+=100
        elif seq==2:
            score+=10
        elif seq==1:
            score+=1

print(score)
