n, m = map(int,input().split())
number = [ int(input()) for _ in range(n)]
quiz=[int(input()) for _ in range(m)]
dic = {}
number.sort()
for i in range(len(number)):
    if number[i] not in dic:
        dic[number[i]]=i
answer=[]




for i in quiz:
    if i not in dic:
        answer.append(-1)
    else:
        answer.append(dic[i])

for i in answer:
    print(i)