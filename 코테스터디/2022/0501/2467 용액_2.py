import sys

n= int(input())
arr= list(map(int,input().split()))
minimum= sys.maxsize
LEFT=0
RIGHT=0


start = 0
end = n-1

while start <end:
    temp = arr[start]+arr[end]
    # print(start,end,temp,minimum,LEFT,RIGHT)
    if minimum>abs(temp):
        LEFT=arr[start]
        RIGHT=arr[end]
        minimum=abs(temp)
    if temp <0:
        start+=1
    else:
        end-=1



print(LEFT,RIGHT)

