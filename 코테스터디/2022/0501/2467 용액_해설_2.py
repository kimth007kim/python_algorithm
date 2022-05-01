import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
answerL = 0
answerR = 0

_min = sys.maxsize

while left<right:
    _sum =arr[left]+arr[right]
    print("left",left,arr[left],"right",right,arr[right])
    print(_sum)
    if abs(_sum)<_min:
        answerL= left
        answerR = right
        _min= abs(_sum)
    if _sum>0:
        right-=1
    elif _sum<0:
        left+=1
    else:
        break
