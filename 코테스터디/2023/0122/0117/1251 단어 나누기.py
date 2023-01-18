word = list(input())
n = len(word)
cand=[]
for i in range(1,n-2):
    for j in range(i+1,n):
        a,b,c="".join(word[:i]), "".join(word[i:j]),"".join(word[j:])
        # print(a,b,c)
        tmp = a[::-1]+b[::-1]+c[::-1]
        cand.append(tmp)

cand.sort()
print(cand[0])
