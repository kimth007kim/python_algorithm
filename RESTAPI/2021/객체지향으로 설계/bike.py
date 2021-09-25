import requests,json
from collections import deque

x_auth_token= "0436cc2bedca3ecb3a39dc731490d671"
url= "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
AVG= 3

class Rent:
    def __init__(self,id,x,y,remain_bike):
        self.id = id
        self.x = x
        self.y = y
        self.remain_bike = remain_bike


# 트럭의 클래스
class Truck:
    def __init__(self, id, x, y, loaded_bike):
        self.id = id
        self.x = x
        self.y = y
        self.loaded_bike = loaded_bike
    def __str__(self):
        return '(id:{}, x:{}, y:{} , loaded_bike: {})'.format(self.id,self.x, self.y,self.loaded_bike)

def MinBike():
    print(1)


def start(number):
    response = requests.post(url+"/start",headers={"X-Auth-Token": x_auth_token,"Content-Type": "application/json"},json={"problem":number})
    return response.json()["auth_key"]


def locations(auth_key):
    response = requests.get(url + "/locations", headers={"Authorization": auth_key, "Content-Type": "application/json"})
    return response.json()["locations"]

def truck(auth_key):
    response = requests.get(url + "/trucks", headers={"Authorization": auth_key, "Content-Type": "application/json"})
    return response.json()["trucks"]

def simulate(auth_key,cmd):
    # print(cmd)
    response = requests.put(url + "/simulate", headers={"Authorization": auth_key, "Content-Type": "application/json"},json={"commands": cmd})
    print(response.json())

    return response.json()["status"]
def score(auth_key):
    # print(url+)
    response = requests.get(url + "/score", headers={"Authorization": auth_key, "Content-Type": "application/json"})
    print("----------------------끝 점수는:",response.json())
# ------------------ 그래프 생성 시작
id_finder={}
graph =[[0]*5 for _ in range(5)]
cnt=0
for i in range(5):
    for j in range(5-1, -1,-1):
        graph[j][i]=Rent(cnt,j,i,4)
        id_finder[cnt]= [j,i]
        # print(j,i,cnt)
        cnt+=1
# -------------------그래프 생성 끝


print(id_finder)
auth_key = start(1)
rest = locations(auth_key)
cars = truck(auth_key)

# ------- 트럭 매핑하기
trucks=[]
for i in cars:
    x,y=id_finder[i['location_id']]
    trucks.append(Truck(i['id'], x, y, i['loaded_bikes_count']))



# 일단 초반에 퍼트려놓는 전략을 사용하자
# command=[]
initial_command=[]
for i in trucks:
    initial_command.append({"truck_id":i.id,"command":[1 for _ in range(i.id)] })
    # command.append(1)


status=simulate(auth_key,initial_command)
while status != "finished":
# for k in range(15):
    print()
    print("------------------시작--------------------")

    location = locations(auth_key)
    vstT = [0 for i in range(5 * 5)]
    for i in location:
        id = i["id"]
        count =i["located_bikes_count"]
        print(id,count)
        command=dict()
        diff=0
        truckId=0
        trucks = truck(auth_key)
        if count>AVG:
            mn=int(1e9)
            for tr in trucks:
                if vstT[tr['id']]==True:
                    continue
                truckCount = tr['loaded_bikes_count']
                if mn > truckCount:
                    truckId=tr['id']
                    mn = truckCount
                    diff = count -AVG
            vstT[truckId]=True
        elif count < AVG:
            mx=-1
            for tr in trucks:
                if vstT[tr['id']]==True:
                    continue
                truckCount = tr['loaded_bikes_count']
                if mx < truckCount:
                    truckId = tr['id']
                    mx = truckCount
                    diff =count -AVG
            vstT[truckId] =True

            fr_x,fr_y= id_finder[truckId]
            to_x,to_y= id_finder[id]
            if diff==0:
                print('차이없음')
                continue
            print("발견!!!!",fr_x,fr_y,to_x,to_y , "차이 ",diff)

    cars = truck(auth_key)
    trucks = []
    # for i in cars:
    #     print(i)
        # x, y = id_finder[i['location_id']]
        # trucks.append(Truck(i['id'], x, y, i['loaded_bikes_count']))
    commands=[]
    for i in range(5):
        commands.append({"truck_id": i, "command":[]})
    status =simulate(auth_key,commands)
    # print(locations(auth_key))


    print("------------------끝--------------------")
score(auth_key)
# 시나리오 1번
# - 서비스 지역의 크기 5*5
# - 자전거 대여 요청 빈도 분당 2건
# - 자전거수: 100대
# - 초기 대여소에 4대씩있음
# - 트럭수: 5대

