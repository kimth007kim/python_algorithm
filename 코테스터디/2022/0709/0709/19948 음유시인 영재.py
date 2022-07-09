import sys

input = sys.stdin.readline
word= input().rstrip()

cnt = int(input())
alpha = {}
blank=0
num = list(map(int,input().split()))
for i in range(len(num)):
    alpha[chr(65+i)]=num[i]
prev=""
for i in word:
    if i==" " and prev!=" ":
        blank+=1
    prev= i
def run(cnt):
    prev = ""
    for i in range(len(word)):
        if word[i] == " ":
            cnt-=1
        if word[i]==prev and word[i]!=" ":
            continue
        if word[i]!=prev and word[i]!=" ":
            now = word[i].upper()
            if alpha[now]<=0:
                return -1
            alpha[now]-=1
            # print(now,alpha)
            prev= word[i]
    result =""
    arr= list(word.split())
    for i in arr:
        if alpha[i[0].upper()]<=0:
            return -1
        result+=i[0].upper()

    return result
            # print(word[i], word[i].islower())

if blank>cnt:
    print(-1)
else:
    answer=run(cnt)
    print(answer)

