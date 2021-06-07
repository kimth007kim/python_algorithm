import sys
import itertools
input=sys.stdin.readline



n,c= map(int,input().split())
data=[]
for i in range(n):
    data.append(int(input()))

array=list(itertools.combinations(data,3))
print(array)
length=len(array[0])


print(data)