def define(w,idx,word_dic):
    w= w.lower()
    w_split= w.split()
    cnt=0
    for i in range(len(w_split)):
        now = w_split[i][0]
        if now==" ":
            continue
        if now not in word_dic:
            word_dic[now]=[idx,cnt]
            return
        cnt+=1+len(w_split[i])

    for k,v in enumerate(w):
        if v not in word_dic:
            if v==" ":
                continue
            word_dic[v]=[idx,k]
            return
n= int(input())
word= []
word_dic={}
for i in range(n):
    tmp= input()
    word.append(tmp)
    define(tmp, i,word_dic)

for i in word_dic:
    k,v=word_dic[i]
    now = word[k]
    # print(now)
    result="["+now[v]+"]"
    word[k]=now[:v]+result+now[v+1:]
    # print(now[:v]+result+now[v+1:])
    # print(result)
    # print(k,v)

for i in word:
    print(i)