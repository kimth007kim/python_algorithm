# word=input()
# word="K1KA5CB7"
word="AJKDLSI412K4JSJ9D"
lenword=len(word)
result=[]
answer=0
real=""

for i in range(lenword):
    if ord(word[i])>=65 and ord(word[i])<=90:
        result.append(word[i])
    else:
        answer+=int(word[i])

result.sort()

for j in range(len(result)):
    real+=result[j]

real+=str(answer)

print(real)