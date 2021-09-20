import json
import requests

# dumps(): Python 객체를 JSON 문자열로 반환
# loads(): JSON파일을 Python 객체로 불러오기

x_auth_token= "0244dcfcd811ba7dabf4b73bb9614074"
contentType= 'application/json'
url ="https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"


def DUMPS(word):
    print(word)
    return json.dumps(word)

def LOADS(word):
    return json.loads(word)


def start_API(url,number):
    target = url +"/start"
    datas = DUMPS({"problem": number})
    start_api = requests.post(target, headers={'X-Auth-Token': x_auth_token, 'Content-Type': contentType}, data=datas)
    result = json.loads(start_api.text)
    return result["auth_key"],result["problem"],result["time"]

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


problem_url="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem%d_day-%d.json"


# print(problem_url)
for i in range(1,3):
    for j in range(1,4):
        print(problem_url,i,j)


# pr1_date_before_1="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-1.json"
# pr1_date_before_2="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-2.json"
# pr1_date_before_3="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem1_day-3.json"
#
#
# pr1_date_before_1="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json"
# pr1_date_before_2="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-2.json"
# pr1_date_before_3="https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-3.json"






# ---------------------------------------------------함수 선언 끝













for i in range(1,3):
    # if i ==1:

    # 시나리오 번호에 맞게 1~2
    auth_key,problem,time=start_API(url,i)
    locations_API(url, auth_key)
    truck_API(url, auth_key)

    simulate_API(url, auth_key)
    # print(auth_key,time)
    # score_API(url, auth_key)
    break
