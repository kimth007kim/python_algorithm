S="John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker"
C="Example"
def solution(S, C):
    answer=[]
    storage=[]
    email= "@"+lowerCase(C)+".com"
    data=list(map(str,S.split(";")))
    word='"'
    for i in range(len(data)):
        word+=data[i]+" "
        tmp=(list(map(str,data[i].split())))
        if len(tmp)==2:
            s1,s2= tmp[1],tmp[0]
        else:
            s1,s2=tmp[2],tmp[0]
        s1,s2= lowerCase(s1),lowerCase(s2)
        result=s1+"_"+s2+email
        if result in storage:
            num=storage.count(result)
            storage.append(result)
            result=s1+"_"+s2+str(num+1)+email
        else:
            storage.append(result)
        if i == len(data)-1:
            word+='<'+result+'>".'
        else:
            word+='<'+result+'>;'
    return word


def lowerCase(st):
    word=""
    for i in range(len(st)):
        tmp= ord(st[i])
        if 65<= ord(st[i]) and 90>= ord(st[i]):
            word+=chr(ord(st[i])+32)
        elif 97<= ord(st[i]) and 122>= ord(st[i]):
            word+=st[i]
    return word

print(solution(S,C))