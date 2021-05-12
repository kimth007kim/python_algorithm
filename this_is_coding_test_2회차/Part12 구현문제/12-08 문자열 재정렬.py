st="K1KA5CB7"
st2="AJKDLSI412K4JSJ9D"

print(chr(57))

def maker(st):
    num=0
    word=[]
    answer=""
    for i in range(len(st)):
        if ord(st[i])<=90 and ord(st[i])>=65:
            word.append(st[i])

        if ord(st[i])<=57 and ord(st[i])>=48:
            # print(st[i])
            num+=int(st[i])
    word.sort()
    for i in word:
        answer+=i
    answer+=str(num)
    # print(num,word)
    print(answer)
maker(st)