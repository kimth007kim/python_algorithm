
import json
import requests

# dumps(): Python 객체를 JSON 문자열로 반환
# loads(): JSON파일을 Python 객체로 불러오기

x_auth_token= "0244dcfcd811ba7dabf4b73bb9614074"
contentType= 'application/json'
url ="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
MAX=5
AVG=3

dx= [0,1,0,-1]
dy= [1,0,-1,0]
mp= [[0 for i in range(MAX)] for j in range(MAX)]



class pos:
    x:int=None
    y: int = None

idxM = [pos() for j in range(MAX*MAX)]


def DUMPS(word):
    print(word)
    return json.dumps(word)

def LOADS(word):
    return json.loads(word)

def mapId(N):
    idx =0
    for i in range(N):
        for j in range(N):
            mp[i][j]=idx
            idxM[idx].x=i
            idxM[idx].y=j
            idx+=1

def start_API():
    target = url +"/start"
    data='{"problem":1}'
    response = requests.post(target, headers={'X-Auth-Token': x_auth_token, 'Content-Type': contentType}, data=data)
    Auth_data = response.json()
    Auth_key= Auth_data.get("auth_key")
    # print(key)
    return Auth_key
    # print(Auth_data)

    # return result["auth_key"],result["problem"],result["time"]

def locations_API(auth_key):
    target = url+"/locations"
    locations_API = requests.get(target, headers={'Content-Type': contentType, 'Authorization': auth_key})
    loc_data = locations_API.json()
    location= loc_data.get("locations")
    return location

def truck_API(auth_key):
    # get방식
    target= url+"/trucks"
    api = requests.get(target,headers={'Content-Type': contentType,'Authorization': auth_key})
    # print(api["trucks"])
    tmp = api.json()
    truck= tmp.get("trucks")
    print(truck)

def simulate_API(url,auth_key,command):
    # put 방식
    data=json.dumps(command)
    target = url+"/simulate"
    response = requests.put(target, headers={'Content-Type': contentType, 'Authorization': auth_key}, data=datas)
    sim_data =  response.json()


def score_API(url,auth_key):
    # get방식
    target=  url+"/score"
    score= requests.get(target, headers={'Content-Type': contentType, 'Authorization': auth_key})
    print(score.text)



Auth_key = start_API()
mapId(MAX)
for i in idxM:
    print(i.x ,i.y)
data = {'commands:{}'}
a_list=[]
# 여기서 부터
location=locations_API(Auth_key)
trucks = truck_API(Auth_key)
vstT = [ 0 for i in range(MAX * MAX)]
vst = [ 0 for i in range(MAX * MAX)]

for i in range(MAX *MAX):
    id = i
    count = location[i].get('located_bikes_count')
    command = dict()
    truckId= 0
    diff = 0
    if count > AVG:
        trucks = truck_API(Auth_key)
    print(count)

problem_url="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem%d_day-%d.json"

