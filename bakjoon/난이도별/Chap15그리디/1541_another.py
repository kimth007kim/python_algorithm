arr =input().split('-')
s=0
for i in arr[0].split('+'):
    s+=int(i)
for j in arr[1:]:
    print(j)
    for k in j.split('+'):
        s -= int(k)
print(s)
