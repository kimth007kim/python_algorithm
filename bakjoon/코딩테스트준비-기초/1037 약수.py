import sys

input = sys.stdin.readline

n= int(input())
data=list(map(int,input().split()))
data.sort()

print(data[0]*data[len(data)-1])
