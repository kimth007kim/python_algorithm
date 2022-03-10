import sys

input = sys.stdin.readline
# k 가진 시간
n,k= map(int,input().split())
# 걷는 시간, 걷는 모금액, 자전거 시간 ,자전거 모금액
arr= []
total=0
time=0


def dfs(minute,money,array):
    global MAX
    if minute>k:
        return
    else:
        MAX=max(money,MAX)
        for i in range(len(array)):
            tmp = array[:i] + array[i + 1:]
            dfs(minute + array[i][0], money + array[i][1], tmp)

for i in range(n):
    t1,m1,t2,m2 = map(int,input().split())
    if t1<t2:
        total+=m1
        time+=t1
        arr.append([t2 - t1, m2 - m1])
    elif t1>t2:
        total += m2
        time += t2
        arr.append([t1 - t2, m1 - m2])
    elif t1==t2:
        total+=max(m1,m2)
        time+=t1

MAX=total
for i in range(len(arr)):
    tmp = arr[:i]+arr[i+1:]
    dfs(time+arr[i][0], total+arr[i][1], tmp)

print(MAX)

