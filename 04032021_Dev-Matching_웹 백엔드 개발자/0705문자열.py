# word="abcdefghkghdefabc"
word="gkjfldjkekasm"
Larr=[]
Rarr=[]
array=[]
def checking(word):
    for i in range(1, len(word)):
        left = word[:i]
        right = word[-i:]
        # print(left, right)
        if left==right:
            Larr.append(left)
            Rarr.append(right)
            return i
    Larr.append(word)
    return len(word)
    # print(left, right)


while len(word)>0:
    a=checking(word)
    word=word[a:]
    word=word[:-a]
    # print(Rarr)

# print(Larr)
# print(Rarr)
for j in range(len(Rarr)-1,-1,-1):
    Larr.append(Rarr[j])
print(Larr)
# print(Rarr)
#     for i in range(1,len(word)):


