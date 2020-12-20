import sys

array=[]
a=int(sys.stdin.readline())
for i in range(a):
    
    b,c=map(int,sys.stdin.readline().split())


    hap= b+c
    array.append(hap)

for i in range(a):
    print(array[i])