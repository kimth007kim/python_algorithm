# num = int(input())

num, comp = map(int,input().split())
A = list(map(int,input().split()))
if len(A) == num:
    for i in A:
        if i<comp:
            print(i,end=" ")