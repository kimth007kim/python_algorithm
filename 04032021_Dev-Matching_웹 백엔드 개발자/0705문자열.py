# word="abcdefghkghdefabc"
word="gkjfldjkekasm"
tmp=[]
while len(word)>0:
    p=len(word)
    print(p)
    for i in range(1,p):
        if i==p-1:
            tmp.append("aa")
            break
        print(i)
        left= word[:i]
        right=word[-i:p]

        # print(word[:i])
        # print(word[-i:p])

        if left==right:
            word=word[i:len(word)-i]
            tmp.append(left)
            print(tmp)
            print("---------발견-----------------")
            print(word)
    break

    # break


    #     print(i,word[i])
    # print(p)
    # break

# print(len(word))
print(tmp)