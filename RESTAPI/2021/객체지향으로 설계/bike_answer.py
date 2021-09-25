import requests
import json
MAX = 5
MMAX = 10000
INF = 99999
AVG = 3

url="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
token="44a1628476646f2b19b8e0d54663382e"

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
mp = [[0 for i in range(MAX)] for j in range(MAX)]


class truck:
    time: int = None
    y: int =None
    x: int =None
    idx: int=None

class pos:
    y:int =None
    x:int =None

class Simulate:
    status: str =None
    time:str =None
    failed_requests_count:str =None
    distance:str =None
    def __init__(self,status,time,failed_requests_count,distance):
        self.status=status
        self.time= time
        self.failed_requests_count= failed_requests_count
        self.distance=distance

def startAPI(number,token):
    response = requests.post(url+"/start", headers={'X-Auth-Token': token,'Content-Type': 'application/json',}, json={"problem":number})
    Auth_data=response.json()
    return Auth_data["auth_key"]

def locationAPI(Auth_key):
    response = requests.get(url+"/locations",headers={ 'Authorization': Auth_key,'Content-Type': 'application/json',})
    location=response.json()["locations"]
    return location

def TrucksAPI(Auth_key):
    headers = {
        'Authorization': Auth_key,
        'Content-Type': 'application/json',
    }
    response = requests.get(url+'/trucks', headers=headers)
    truck_data = response.json()
    truck_json = json.loads(json.dumps(truck_data))
    truck = truck_json.get("trucks")
    return truck

def score(auth_key):
    # print(url+)
    response = requests.get(url + "/score", headers={"Authorization": auth_key, "Content-Type": "application/json"})
    return response.json()["score"]

def SimulateAPI(Auth_key,trucks,command):
    headers = {
        'Authorization': Auth_key,
        'Content-Type': 'application/json',
    }
    data = json.dumps(command)
    response = requests.put(url + '/simulate', headers=headers, data=data)
    sim_data = response.json()
    sim_json = json.loads(json.dumps(sim_data))
    location = locationAPI(Auth_key)
    trucks = TrucksAPI(Auth_key)
    simulate=Simulate(
        sim_json.get('status'),
        sim_json.get('time'),
        sim_json.get('failed_requests_count'),
        sim_json.get('distance')
    )

    return simulate.status

def move(fr=pos(),to=pos(),w=0,id=0):
    commandO=dict()
    cmd=list()

    # 상차
    if w>0:
        for  i in range(w):
            cmd.append(5)

    if fr.x<to.x:
        for i in range(to.x-fr.x):
            cmd.append(2)

    if fr.x>to.x:
        for i in range(fr.x-to.x):
            cmd.append(4)

    if fr.y<to.y:
        for i in range(to.y-fr.y):
            cmd.append(1)


    if fr.y>to.y:
        for i in range(fr.y-to.y):
            cmd.append(3)

    if w<0:
        for i in range(-w):
            cmd.append(6)


    commandO["truck_id"]=id
    commandO["command"]=cmd

    print(commandO)
    return commandO


def mapId(N):
    idx=0
    for i in range(N):
        for j in range(N):
            mp[i][j]=idx
            idxM[idx].x=i
            idxM[idx].y=j
            idx+=1



idxM = [pos() for j in range(MAX*MAX)]


Auth_key = startAPI(1,token)


mapId(MAX)

data={'commands':{}}
while True:
# for _ in range(3):
    print()
    print("---------------------------------- 시작 --------------------------------")
    a_list=[]
    location=locationAPI(Auth_key)
    vstT = [0 for i in range(MAX*MAX)]
    vst= [0 for i in range(MAX*MAX)]
    for i in range(MAX*MAX):
        id=i
        count = location[i]['located_bikes_count']
        command= dict()
        truckId=0
        diff=0
        if count >AVG:
            trucks =TrucksAPI(Auth_key)
            mn= INF
            for tr in trucks:
                if vstT[tr['id']]==True:
                    continue
                truckCount = tr['loaded_bikes_count']
                if mn > truckCount:
                    truckId = tr['id']
                    mn= truckCount
                    diff = count -AVG
            vstT[truckId]=True
            # print(vstT)
        elif count <AVG:
            mx=-1
            for tr in trucks:
                if vstT[tr['id']]==True:
                    continue
                truckCount = tr['loaded_bikes_count']
                if mx<truckCount:
                    truckId= tr['id']
                    mx= truckCount
                    diff = count -AVG
            vstT[truckId] = True
        print(truckId,diff,vstT)
        fr=pos()
        fr = idxM[trucks[truckId]['location_id']]
        to =pos()
        to= idxM[id]
        print(fr.x ,fr.y,"=================>",to.x,to.y)
        if diff==0:
            continue
        command = move(fr,to,diff,truckId)
        a_list.append(command)
    data["commands"]=a_list
    if SimulateAPI(Auth_key,trucks,data)=="finished":
        break








