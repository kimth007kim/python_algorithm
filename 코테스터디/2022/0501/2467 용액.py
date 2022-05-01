import sys

n= int(input())
arr = list(map(int,input().split()))

start = 0
end = len(arr)-1

answerL = 0
answerR = 0


MIN = sys.maxsize
while start<end:
    tmp = arr[start]+arr[end]
    if abs(tmp)<MIN:
        answerL= start
        answerR = end
        tmp = abs(tmp)
    if tmp>0:
        end-=1
    elif tmp<0:
        start+=1
    else:
        break


