# money= int(input())
money=1260
cnt=0

coin= [500, 100 ,50 ,10]

for i in range(len(coin)):
    cnt += money // coin[i]
    money= money % coin[i]
print(cnt)