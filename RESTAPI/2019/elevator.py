import requests
from pprint import pprint


url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    tmp=requests.post(uri).json()
    return tmp

def onCall(token):
    uri =url +"/oncalls"
    tmp=  requests.get(uri,headers={"X-Auth-Token":token})
    return tmp.json()

def action(token,cmd):
    uri = url+"/action"
    tmp= requests.post(uri, headers={"X-Auth-Token": token}, json= {"commands":cmd})
    print("action후의 값입니다.",tmp.json())
    return tmp.json()

def p0_simulator():
    user = 'tester'
    problem = 0
    count = 1

    cnt=0

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))
    oncall_res = onCall(token)
    while True:
        print("**********************************************")
        print("----------------  cnt",cnt,"----------------")
        print("**********************************************")
        print()
        oncall_res=onCall(token)
        print("--     onCall 한 결과    --", oncall_res)
        origin_calls = oncall_res["calls"]
        elevators = oncall_res["elevators"]
        # print(origin_calls,elevators)
        action_bucket = []
        will_enter_by_calls =set()
        will_exit_by_pasengers=set()
        # print("elevators:",elevators)
        # for elevator_id in range(4):
        floor = elevators[0]['floor']
        passengers = elevators[0]["passengers"]
        # print("----passenger----",passengers)
        status = elevators[0]["status"]
        if status == "STOPPED":
            for passenger in passengers:
                if passenger['end']==floor:
                    action_bucket.append({'elevator_id': 0, 'command': 'OPEN'})
                    break
            else:
                for call in origin_calls:
                    if len(passengers) <8 and call["start"]==floor:
                        action_bucket.append({'elevator_id':0,'command':'OPEN'})
                        break
                else:
                    for passenger in passengers:
                        if passenger['end']>floor:
                            action_bucket.append({'elevator_id':0,'command':'UP'})
                            break
                        else:
                            action_bucket.append({'elevator_id': 0, 'command': 'DOWN'})
                            break
                    else:
                        for call in origin_calls:
                            if call["start"]>floor:
                                action_bucket.append({'elevator_id': 0, 'command': 'UP'})
                                break
                            else:
                                action_bucket.append({'elevator_id': 0, 'command': 'DOWN'})
                                break
                        else:
                            action_bucket.append({'elevator_id': 0, 'command': 'STOP'})
                            print("말도 안됨")
        elif status == "OPENED":
            call_ids=[]
            for passenger in passengers:
                if not passenger["id"] in will_exit_by_pasengers and passenger["end"]==floor:
                    call_ids.append(passenger["id"])
                    will_exit_by_pasengers.add(passenger["id"])
            if len(call_ids):
                action_bucket.append({'elevator_id': 0, 'command': 'EXIT', 'call_ids':call_ids})
            else:
                call_ids=[]
                print("pass nums: ", len(passengers))
                for call in origin_calls:
                    if len(passengers)==8:
                        break
                    if not call["id"] in will_exit_by_pasengers and call["start"]==floor:
                        print(call["id"])
                        call_ids.append(call["id"])
                        will_enter_by_calls.add(call["id"])
                    if len(call_ids)+len(passengers) >=8:
                        break
                if len(call_ids):
                    action_bucket.append({'elevator_id': 0, 'command': 'ENTER', 'call_ids':call_ids})
                else:  #내릴사람도 탈사람도 없으면 닫기
                    action_bucket.append({'elevator_id': 0, 'command': 'CLOSE'})
        elif status=="UPWARD":
            for passenger in passengers:
                # 내릴 승객이있으면
                if passenger['end']==floor:
                    # 문열기
                    action_bucket.append({'elevator_id': 0, 'command': 'STOP'})
                    break
            # 없으면
            else:
                for call in origin_calls:
                    if call['start']==floor:
                        # 열어라
                        action_bucket.append({'elevator_id': 0, 'command': 'STOP'})
                        break
                # 아니면
                else:
                    # 올라가라
                    action_bucket.append({'elevator_id': 0, 'command': 'UP'})
        elif status == "DOWNWARD":
            for passenger in passengers:
                #내릴승객이 있으면
                if passenger['end']==floor:
                    # 뮨을 열어라
                    action_bucket.append({'elevator_id': 0, 'command': 'STOP'})
                    break
            else:
                for call in origin_calls:
                    if call['start']==floor:
                        #열어라
                        action_bucket.append({'elevator_id': 0, 'command': 'STOP'})
                        break
                #아니면
                else:
                    #내려가라
                    action_bucket.append({'elevator_id': 0, 'command': 'DOWN'})


        cnt+=1
        print("--action_bucket 에 담긴것들--",action_bucket)
        response = action(token,action_bucket)
        print("action취하고 난후에 보기")
        pprint(response)
        if response["is_end"]:
            print("__________________________________________________끝__________________________")
            break

if __name__ == '__main__':
    p0_simulator()