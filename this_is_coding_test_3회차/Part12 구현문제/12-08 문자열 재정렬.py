NUM=0
WORD=[]

n = input()

for i in range(len(n)):
    if n[i].isalpha():
        WORD.append(n[i])
    else:
        NUM+=int(n[i])
WORD.sort()
answer="".join(WORD)
answer+=str(NUM)

print(answer)