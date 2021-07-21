import sys
input = sys.stdin.readline

n,k= map(int,input().split())
d=[[0]*(k+1) for _ in range(n+1)]
# print(d)
for i in range(1,n+1):
    item,value= map(int,input().split())
    for j in range(1,k+1):
        print(item,j)
        if item>j:
            d[i][j]=d[i-1][j]
        else:
            d[i][j] =max(d[i-1][j],d[i-1][j-item]+value)
            print(d)
    # print(d)
        # print(d)
        # print()

# for i in range(n):
#     w,v=map(int,input().split())
#     d[w]= max(d[w],v)
#     arr.append([w,v])
#
#
# for i in range(1,limit+1):
#     for a,b in arr:
#         if i+a>limit:
#             continue
#         else:
#             d[i+a] =max(d[i+a],d[i]+b)
#
# MAXVALUE= max(d)
# d[limit]=max(d[limit],MAXVALUE)
#
# print(d[limit])