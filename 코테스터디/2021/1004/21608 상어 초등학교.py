n= int(input())

dx= [0,1,0,-1]
dy= [1,0,-1,0]



def finder(arr,number,numberList):
    available=[]
    for i in numberList:
        if Students[i-1].x != None and Students[i-1].y != None:
            available.append([Students[i - 1].x,Students[i-1].y])

    if len(available)==0:
        MAX=0
        # 좋아하는 학생이 배치되지 않았을때
        for i in range(n):
            for j in range(n):
                if arr[i][j]!=0:
                    continue
                cnt =0
                for k in range(4):
                    nx= dx[k]+i
                    ny= dy[k]+j
                    if 0<=nx<n and 0<=ny<n:
                        if arr[nx][ny]==0:
                            cnt+=1
                if cnt>MAX:
                    MAX=cnt
                    tx=i
                    ty=j
        arr[tx][ty]=number
        Students[number-1].x=tx
        Students[number-1].y=ty

    else:
        MAX=0
        data=[]
        for i in range(n):
            for j in range(n):
                cnt=0
                if arr[i][j]==0:
                    for k in range(4):
                        nx = dx[k] + i
                        ny = dy[k] + j
                        if 0 <= nx < n and 0 <= ny < n:
                            temp=arr[nx][ny]
                            if temp in numberList:



                                print(nx,ny ,arr[nx][ny],numberList)
                                cnt+=1
                if cnt>0:
                    if MAX<cnt:
                        MAX=cnt
                    data.append([i,j,cnt])

        print("num = ",num,"data = ",data)

        if len(data)!=0:
            tmp = []
            for x,y,cnt in data:
                print(x,y,cnt)
                counter=0
                if cnt==MAX:
                    for i in range(4):
                        nx=dx[i]+x
                        ny=dy[i]+y
                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]==0:
                            counter+=1
                tmp.append([counter,x,y])
            print(num,tmp)
            tmp.sort(key= lambda x:(-x[0],x[1],x[2]))
            print(num,tmp)
            for i in arr:
                print(i)
            arr[tmp[0][1]][tmp[0][2]]=num
            Students[num-1].x=tmp[0][1]
            Students[num-1].y=tmp[0][2]
        else:
            for i in range(n):
                for j in range(n):
                    if arr[i][j]==0:
                        arr[i][j]=number




arr = [[0]*n for _ in range(n)]
dict = {}

class student:
    def __init__(self):
        self.x= None
        self.y= None
    def __str__(self):
        return "x:{} 와 y:{}".format(self.x, self.y)

Students=[]
for i in range(n*n):
    Students.append(student())


for i in range(n*n):
    num,a,b,c,d= map(int,input().split())
    dict[num]=[a,b,c,d]
    finder(arr,num,dict[num])

score= 0

for i in range(n):
    for j in range(n):
        seq=0
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0 <= nx < n and 0 <= ny < n:
                tmp=arr[nx][ny]
                if tmp in dict[arr[i][j]]:
                    seq+=1
        if seq==0 or seq==1:
            score+=1
        elif seq==2:
            score+=10
        elif seq==3:
            score+=100
        else:
            score+=1000

print(score)



# 1. 비어있는 칸중에서 좋아하는 학생이 가장 많은칸으로 자리를 이동
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 이동
# 3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.



