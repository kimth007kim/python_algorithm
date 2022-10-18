from collections import defaultdict
dic = defaultdict(int)
for i in range(1,31):
    dic[i]

# print(dic)
for i in range(28):
    tmp = int(input())
    dic[tmp]+=1

for i in range(1,31):
    if dic[i]==0:
        print(i)