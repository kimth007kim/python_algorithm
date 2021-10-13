import sys
input =sys.stdin.readline

def AEIOU(word):
    mo=0
    ja=0
    candidate= ['a','e','i','o','u']
    for i in word:
        if i in candidate:
            mo+=1
        else:
            ja+=1
    if mo>=1 and ja>=2:
        return True
    else:
        return False

def dfs(ch,idx,word,data):
    if len(word)==l:
        if AEIOU(word):
            answer.append(word)
        return
    for i in range(idx+1,len(data)):
        previous =word
        word+= data[i]
        dfs(ch,i,word,data)
        word=previous

l,c =map(int,input().split())
data=list(input().split())
data.sort()


answer=[]


for i in range(len(data)):
    ch=data[i]
    word=""
    word+=ch
    dfs(ch,i,word,data)

answer.sort()
for i in answer:
    print(i)