from itertools import permutations
from copy import deepcopy

def show(arr):
    for i in arr:
        print(i)
    print()

N,M,K= map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
rcs= [ list(map(int,input().split())) for _ in range(K)]
answer=int(1e9)
for p in permutations(rcs,K):
    copy_arr = deepcopy(arr)
    for r,c,s in p:
        r-=1
        c-=1
        print(r-s,c-s,r+s,c+s)
        for n in range(s,0,-1):
            tmp = copy_arr[r-n][c+n]
            # print("tmp[{}-{}] [{}+{}]={} ".format(r,n,c,n,tmp))
            # print(copy_arr[r-n][c-n+1:c+n+1])
            copy_arr[r-n][c-n+1:c+n+1]=copy_arr[r-n][c-n:c+n]
            # print(copy_arr[r-n][c-n+1:c+n+1])
            for row in range(r-n,r+n):
                # print(row,c-n,copy_arr[row][c-n],"   ",row+1,c-n,copy_arr[row+1][c-n])
                copy_arr[row][c-n]=copy_arr[row+1][c-n]
            copy_arr[r+n][c-n:c+n]=copy_arr[r+n][c-n+1:c+n+1]
            for row in range(r+n,r-n,-1):
                copy_arr[row][c+n]=copy_arr[row-1][c+n]
            copy_arr[r-n+1][c+n]=tmp

            show(copy_arr)

    # for pp in copy_arr:
    #     print(pp)
    # print()
    for i in copy_arr:
        answer= min(answer,sum(i))

print(answer)
