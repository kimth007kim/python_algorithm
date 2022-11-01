# D: D 는 n을 두 배로 바꾼다.
# 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
# 그 결과 값(2n mod 10000)을 레지스터에 저장한다.

# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
# n이 0 이라면 9999 가 대신 레지스터에 저장된다.

# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.

# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.


from collections import deque,defaultdict
import sys

input =sys.stdin.readline


def calcL(n):
    front =n %1000
    back =n//1000
    res=front *10+back
    return res

def calcR(n):
    front = n%10
    back = n//10
    res= front * 1000+back
    return res

def register(start,end):
    q = deque()
    visit=[False]*10001
    q.append([start,""])
    visit[start]=True
    while q:
        now, word = q.popleft()
        if now==end:
            return word

        d= now*2
        if d>9999:
            d=d%10000
        if visit[d]==False:
            q.append([d,word+"D"])
            visit[d]=True

        if now ==0:
            s=9999
        else:
            s=now-1
        if visit[s]==False:
            visit[s]=True
            q.append([s,word+"S"])

        l=calcL(now)
        r=calcR(now)

        if visit[l]==False:
            q.append([l,word+"L"])
            visit[l]=True
        if visit[r]==False:
            q.append([r,word+"R"])
            visit[r]=True
        # break

for i in range(int(input())):
    start,end= map(int,input().split())
    # print(start,end)
    answer =register(start,end)
    print(answer)
    # break
