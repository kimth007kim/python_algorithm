def dfs(number):
    global cnt
    for i in range(1, 4):
        if number+i == n:
            cnt += 1
        elif number+i < n:
            dfs(i+number)
        # else:
        #     return

answer=[]
for _ in range(int(input())):
    cnt=0
    n=int(input())
    for i in range(1, 4):
        if i == n:
            cnt += 1
        if i < n:
            dfs(i)
    answer.append(cnt)

for i in answer:
    print(i)