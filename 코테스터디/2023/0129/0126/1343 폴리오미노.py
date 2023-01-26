word = input()

word=word.replace("XXXX","AAAA")
word=word.replace("XX","BB")

flag= True
for i in range(len(word)):
    if word[i]=="X":
        flag=False
        break


if flag==True:
    print(word)
else:
    print(-1)