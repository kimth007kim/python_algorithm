# n,m = map(int,input().split())
# data=[]
# for i in range(n):
#     data.append(list(map(int,input().split())))
# cmd=int(input())
n,m=4,4
data=[[9, 14, 29, 7], [1, 31, 6, 13], [21, 26, 40, 16], [8, 38, 11, 23]]

prefix=[[0] for _ in range(n)]

for i in range(len(data)):
    sum_value=0
    for j in data[i]:
        sum_value += j
        prefix[i].append(sum_value)
        print(prefix[i],j)
    print(prefix)


print(prefix)
# print(data)