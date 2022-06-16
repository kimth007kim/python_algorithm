import sys

input =sys.stdin.readline
t = int(input())

num_dict={}
def dfs(arr,total,cnt):
    global num_dict
    # print(arr,total)
    if cnt==3:
        num_dict[total]=arr
        # print(num_dict)
        return
    for i in num:
        if total+i<1000:
            dfs(arr+[i],total+i,cnt+1)
num = []
for now in range(2,1000):
    bool=False
    for i in range(2,now-1):
        if now !=i and  now % i ==0:
            bool=True
            break
    if bool==False:
        num.append(now)

for i in num:
    dfs([i],i,1)

# print(num_dict)


for i in range(t):
    n = int(input())
    if n in num_dict:
        tmp = num_dict[n]
        tmp.sort()
        print(*tmp)
    else:
        print(0)