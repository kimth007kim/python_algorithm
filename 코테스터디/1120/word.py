import random

f = open("word.txt", 'r',encoding='UTF8')
lines = f.readlines()
dict = {}
storage =[]
score=0
total = 0
cnt=0

for line in lines:
    line = line.strip()
    a,b = line.split()
    dict[a]=b
    storage.append(a)
    cnt+=1
f.close()


sampleList = random.sample(storage, cnt)

for i in sampleList:
    print(i)
    answer= input()
    if answer == dict[i]:
        score+=1


print("당신의 점수는 {}점 입니다!".format(score))