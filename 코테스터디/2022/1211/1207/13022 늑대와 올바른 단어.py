# from collections import defaultdict
#
# dic= defaultdict(int)
# dic["w"]
# dic["o"]
# dic["l"]
# dic["f"]

word= input()
prev=""
# print(word)
flag= True
correct=False
w,o,l,f=0,0,0,0
for i in range(len(word)):
    # print(i,word[i])
    if word[i]=="w":
        if prev=="" or prev=="f" or prev=="w":
            prev = word[i]
            w+=1
        else:
            flag=False
            break
    if word[i]=="o":
        if (prev=="w" or prev=="o" )and w>o:
            prev = word[i]
            o+=1
        else:
            flag=False
            break
    if word[i]=="l":
        if (prev=="o" or prev=="l") and o>l:
            prev = word[i]
            l+=1
        else:
            flag=False
            break
    if word[i]=="f":
        if (prev=="l" or prev=="f") and l>f:
            prev = word[i]
            f+=1
            if l==f:
                w,o,l,f=0,0,0,0
                correct=True
        else:
            flag=False
            break
if correct==False:
    flag=False

if flag:
    print(1)
else:
    print(0)