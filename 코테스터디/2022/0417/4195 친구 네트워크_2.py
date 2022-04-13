# import sys
#
# input =sys.stdin.readline

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,score,a,b):
    # global answer
    A = find_parent(parent, a)
    B = find_parent(parent, b)
    if A!=B:
        parent[A]=B
        score[B]+=score[A]
        # answer.append(score[B])
        print(score[B])
    # else:
    #     parent[B]=A
    #     score[A]+=score[B]
    #     # answer.append(score[A])
    #     print(score[A])
    # print(A,B)
    # print(score)

# answer=[]
for _ in range(int(input())):
    friends={}
    user,number={},{}
    arr=[]
    cnt=0

    f= int(input())
    for i in range(f):
        a,b = map(str,input().split())
        if a not in user:
            user[a]=cnt
            number[user[a]]=1
            cnt+=1
        if b not in user:
            user[b]=cnt
            number[user[b]]=1
            cnt+=1
        arr.append([a,b])
    parent=[0]*(len(user))
    # score=[1]*(len(user))
    for i in range(len(parent)):
        parent[i]=i
    for a,b in arr:
        union_parent(parent,number,user[a],user[b])
# for i in answer:
#     print(i)