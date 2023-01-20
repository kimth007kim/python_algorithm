import sys
from collections import deque

input = sys.stdin.readline

word = input().rstrip()
n=len(word)
cnt= 0
w=""
for i in range(n):
    if word[i]=="X":
        cnt=i
        # w+="X"
        break
    else:
        w+="."
tmp=0
prev= ""
flag=True
for i in range(cnt,n):
    if word[i]=="X":
        tmp+=1
    else:
        if prev=="X":
            if tmp%2!=0:
                flag=False
        tmp=0


    prev= word[i]
if flag==False:
    print(-1)
else:
    cand=[]
    q=deque()
    q.append([w,cnt])

    while q:
        # print(q)
        w,num= q.popleft()
        if num==n:
            cand.append(w)
            continue
        if word[num]==".":
            tmp="."
            cnt=1
            for i in range(num+1,n):
                if word[i]==".":
                    tmp+="."
                    cnt+=1
                else:
                    break
            q.append([w+tmp,num+cnt])
            continue
        if num+3<n:
            tmp=0
            for i in range(num,num+4):
                if word[i]=="X":
                    tmp+=1
            if tmp==4:
                q.append([w+"AAAA",num+4])
        if num+1<n:
            tmp=0
            for i in range(num,num+2):
                if word[i]=="X":
                    tmp+=1
            if tmp==2:
                q.append([w+"BB",num+2])

    if len(cand)==0:
        print(-1)
    else:
        cand.sort()
        print(cand[0])