# 3:40분 시작 4시 11분해결

# H: 호텔층수 W: 각층의 방수 N: 몇번손님
# 입력: 6 12 10 출력: 402
data=[]
cnt=int(input())
for i in range(cnt):
    H,W,N= map(int,input().split())
    floor = N % H
    room = N // H+1
    if floor==0:
        floor =H
        room= N//H
    data.append(floor *100+ room)
for datas in data:
    print(datas)
