n= int(input())

dx= [0,1,0,-1]
dy= [1,0,-1,0]

def finder(arr,numberList):
    available=[]
    for i in numberList:
        print(i-1 ,Students[i-1].x)
        if Students[i-1].x != None and Students[i-1].y != None:
            available.append([Students[i - 1].x,Students[i-1].y])
    print("available",available)
    for i in range(n):
        for j in range(n):
            print(i,j)


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

for i in Students:
    print(i)

for i in range(n*n):
    num,a,b,c,d= map(int,input().split())
    dict[num]=[a,b,c,d]
    finder(arr,dict[num])



# 1. 비어있는 칸중에서 좋아하는 학생이 가장 많은칸으로 자리를 이동
# 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 이동
# 3. 2를 만족하는 칸도 여러개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


for n in dict:
    print(n,dict[n])


