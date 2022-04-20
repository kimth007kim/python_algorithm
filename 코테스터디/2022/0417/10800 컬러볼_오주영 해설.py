from collections import defaultdict
import sys

input= sys.stdin.readline

n= int(input())
ball=[]
color_dict=defaultdict(int)

for i in range(n):
    c,size=map(int,input().split())
    color_dict[c]
    ball.append([size,c,i])

ball.sort()

res=[0]*(n+1)
total =0
cnt=0

for i in range(n):
    while ball[cnt][0]<ball[i][0]:
        total+=ball[cnt][0]
        color_dict[ball[cnt][1]]+=ball[cnt][0]
        cnt+=1
        print(color_dict)
    res[ball[i][2]]= total-color_dict[ball[i][1]]
for i in range(n):
    print(res[i])