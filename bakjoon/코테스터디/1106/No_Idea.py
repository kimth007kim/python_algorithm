n, m = map(int, input().split())
person = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dic = {}
for i in a:
    dic[i] = 1
for i in b:
    dic[i] = -1

score = 0

for i in person:
    if i in dic:
        score += dic[i]

print(score)