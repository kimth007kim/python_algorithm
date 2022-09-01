import random
percent = [100,81,64,50,26,15,7,4,2]

def intToTime(time):
    year= time//(30*12*24*60*60)
    time= time%(30*12*24*60*60)
    month= time//(30*24*60*60)
    time= time%(30*24*60*60)
    day = time//(24*60*60)
    time=time%(24*60*60)
    hr = time//(60*60)
    time = time%(60*60)
    mm= time//60
    time= time%60
    print("강화 한번에 10초라는 가정하에 24시간 내내 강화만해서")
    print("1~10카 스트레이트 성공까지 {}년 {}달 {}일 {}시간 {}초 가 소요되었습니다.".format(year,month,day,hr,mm,time))



def inhance(now):
    if now==10:
        return now
    ran=random.randrange(0,101)
    if ran>percent[now-1]:
        print(ran,"터짐 요구치",percent[now-1])
        return now
    print(now+1,"강화성공 요구치=",percent[now-1],"나온값",ran)
    return inhance(now+1)

MAX=0
cnt=0
time =0

while MAX<10:
    now = inhance(1)
    cnt+=1
    time +=10*(now-1)
    MAX=max(MAX,now)

print(cnt,"번 돌려서 겨우 되셨네요 ㅎㅎ")
intToTime(time)