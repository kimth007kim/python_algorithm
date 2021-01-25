
sik= input().split('-')
print(sik)
index=[]
slen= len(sik)
word=''
if slen>1:
    for j in range(slen):
        if j !=0:
            word+='-('
            word+=sik[j]
            word+=')'
        else:
            word+=sik[j]
else:
    word+=str(sik[0])


print(eval(word))
