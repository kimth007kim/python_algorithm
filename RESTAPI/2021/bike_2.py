
import json
import requests

# dumps(): Python 객체를 JSON 문자열로 반환
# loads(): JSON파일을 Python 객체로 불러오기

x_auth_token= "0244dcfcd811ba7dabf4b73bb9614074"
contentType= 'application/json'
url ="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"
MAX=5
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

def locations_API(url,auth_key):
    target = url+"/locations"
    locations_API = requests.get(target, headers={'Content-Type': contentType, 'Authorization': auth_key})
    print(locations_API.text)


def truck_API(url,auth_key):
    # get방식
    target= url+"/trucks"
    api = requests.get(target,headers={'Content-Type': contentType,'Authorization': auth_key})
    # print(api["trucks"])
    tmp = LOADS(api.text)
    arr= tmp["trucks"]
    for i in arr:
        print(i)
    # print(arr)
    # print(api.text["trucks"])

def simulate_API(url,auth_key):
    # put 방식
    data={ "truck_id": 0, "command": [2, 5, 4, 1, 6] }
    datas=DUMPS(data)
    target = url+"/simulate"
    simulate = requests.put(target, headers={'Content-Type': contentType, 'Authorization': auth_key}, data=datas)
    print(simulate)
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
location=1



problem_url="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem%d_day-%d.json"

