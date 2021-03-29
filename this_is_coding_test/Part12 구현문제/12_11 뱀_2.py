# Dummy 라는 도스게임 
# 뱀은 매초마다 이동

# n번째 보드의 크기
# 6         n번째 보드의 크기
# 3         k개 사과의 갯수
# 3 4       사과위치1
# 2 5       사과위치2
# 5 3       사과위치3
# 3         방향변환정보 오른쪽D또는 왼쪽L 로 90도 회전
# 3 D       3초후에 오른쪽으로회전
# 15 L
# 17 D

# 방향변환정보
#  오른쪽D 로 90도 회전
#  왼쪽L 로 90도 회전

n= int(input())
k= int(input())
field = [[0]*n for _ in range(n)]
apple=[]
direction=[]
for j in range(k):
    a,b = map(int,input().split())
    apple.append((a,b))
    field[a][b]=1


l= int(input())
for i in range(l):
    c,d= map(str,input().split())
    c= int(c)
    direction.append((c,d))
print(apple)
print(direction)


x=0
y=0
dx=[1,0,-1,0]
dy=[0,-1,0,1]
cnt = 0
dcnt=0

while True:
    x+=dx[dcnt]
    y+=dy[dcnt]
    if y >= n or y < 0 or x >= n or x < 0:
        break
    field[y][x]=cnt
    cnt+=1

print(cnt)
for j in field:
    print(j)
