import requests

INF=int(1e9)

url = 'http://localhost:8000'


def findStorage(id,storage):
    print("                     ",id)
    for i in storage:
        print(i)
        # if len(i)!=0:
        #     continue
        # else:
        #     if id in i:
        #         return False
    return True

def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()

def elevator_simulator():
    IS_ENTER={}
    problem=0
    MAX_HEIGHT= 5
    MAX_PEOPLE=8
    count =2
    user = "KIM"
    storage=[]
    for i in range(count):
        storage.append({})
    timestamp=0
    token= start(user,problem,count)["token"]
    while True:
    # while timestamp<15:

        print("-----------------------------",timestamp," 시작-------------------")

        command=[]
        oncall_res=oncalls(token)
        calls= oncall_res["calls"]
        findStorage(calls, storage)
        for call in calls:
            counter=0
            if call["id"] not in IS_ENTER:
                for k in calls:
                    if k["id"] == call["id"]:
                        print("숫자가 추가된다!")
                        counter += 1
                IS_ENTER[call["id"]]=counter

        print(IS_ENTER)
        print("   콜:",calls)
        oncall_elevator = oncall_res["elevators"]
        print("   엘리베이터:",oncall_elevator)

        for call in calls:
            print("                 !!!                ", call)
            print("                 !!!                ", call["id"])

            if len(passenger) < 8 and findStorage(call["id"], storage):
                people_count = 0
                for k in calls:.

                    print(k, k["id"], people_count)
                    if k["id"] == people_count:
                        print("숫자가 추가된다!")
                        people_count += 1
                # passe


        for i in oncall_elevator:
            id= i["id"]
            floor=i["floor"]
            status= i["status"]
            passengers=i["passengers"]
            print(" 현재 승객수는? ", len(passengers))
            print("지금 계시는 층은 " ,floor ,"층입니다.")
            print("  승객",passengers)


            if status=="STOPPED":
                for passenger in passengers:
                    print("passenger 안에 탐색", passenger)
                    if passenger['end']==floor:
                        print("내릴 사람이있으면 연다")

                        command.append({'elevator_id': id, "command": 'OPEN'})
                        break
                else:
                    for call in calls:
                        if len(passengers)<8 and call["start"]==floor:
                            print("탈사람이 있다면 연다!")
                            command.append({'elevator_id': id, "command": 'OPEN'})
                            break
                    else:
                        print("내릴사람도 없고 탈사람도없다.")
                        for passenger in passengers:
                            print("판독중 어디로갈까나",passenger)
                            if passenger['end']>floor:
                                print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑   내릴 사람도 없고 탈 사람도 없다면 출발지가 높으면 올라갑시다.    ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
                                command.append({'elevator_id': id, "command": 'UP'})
                                break
                            else:
                                print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  내릴 사람도 없고 탈 사람도 없다면 출발지가 낮으면 내려갑시다.    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
                                command.append({'elevator_id': id, "command": 'DOWN'})
                                break
                        else:
                            print("엘리베이터에는 사람이 없네요!")
                            for call in calls:
                                if call["start"]>floor:
                                    command.append({'elevator_id':id ,"command":"UP"})
                                    break
                                else:
                                    print("출발지가 낮으면 내려가세요!")
                                    command.append({'elevator_id':id ,"command":"DOWN"})
                                    break
                            else:
                                print("태울방향 없고 타고있는 닝겐도없다")
                                command.append({'elevator_id': id, "command": "STOP"})
            elif status == "OPENED":
                # if len(calls)==0
                print("문열림 상태")
                call_ids = []
                count_same_id = 0
                for passenger in passengers:
                    if passenger["end"]==floor:
                        will_out = passenger["id"]
                        for k in passengers:
                            print(k, k["id"], will_out)
                            if k["id"] == will_out:
                                count_same_id += 1
                        print("내리실 분의 id----------------",will_out,count_same_id)
                        print(" 문이 열린 상태에 내릴 분이 계심")
                        for k in range(count_same_id):
                            call_ids.append(passenger["id"])
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~call_ids",call_ids)
                        command.append({"elevator_id":id,"command":"EXIT","call_ids":call_ids})
                        break
                else:
                    call_ids=[]
                    count_same_id=0
                    for call in calls:
                        if call["start"]==floor:
                            will_in=call["id"]
                            for k in calls:
                                print(k, k["id"], will_in)
                                if k["id"]== will_in:
                                    print("숫자가 추가된다!")
                                    count_same_id+=1
                            print("문이 열린 상태에서 타실분이 계심.")
                            print("이번에 타실 승객인 id가 ",will_in,"인 승객은", count_same_id," 명 계십니다.")

                            print(len(passengers))
                            if len(passengers)+ count_same_id>8:
                                command.append({'elevator_id': id, "command": "CLOSE"})
                                break
                            else:
                                for k in range(count_same_id):
                                    call_ids.append(call["id"])
                                command.append({"elevator_id": id, "command": "ENTER","call_ids":call_ids})
                                break
                    else:
                        print("타실분도 안계시고 내리실분도 안계심")
                        print(" 임시적으로 닫는걸로 설계")
                        command.append({'elevator_id': id, "command": "CLOSE"})
                        break
            elif status == "UPWARD":
                print("======================================================")
                print("======================문제의 부분============================")
                print("======================================================")
                print("======================================================")
                for passenger in passengers:
                    if passenger["end"]==floor:
                        print("올라가는 도중에 내리실 분이 계시는군요!")
                        command.append({'elevator_id': id, "command": "STOP"})
                        break
                    # print("여기다!!!!!!! ",passenger)
                else:
                    print("올라가는데 내리시는 분은 없네요")
                    for call in calls:
                        print(call)
                    print("올라가는중이네요")
                    print("임시로 상태를 STOP으로 바꿔놓자고요")
                    command.append({'elevator_id': id, "command": "STOP"})
                    break
            elif status =="DOWNWARD":
                print("내려가는중이네요")
                print("임시로 상태를 STOP으로 바꿔놓자고요")
                command.append({'elevator_id': id, "command": "STOP"})
                break

        print("들어가야할 값들 출력",token,command)
        response =action(token,command)
        timestamp+=1
        print("    액션후 결과값:",response)
        if response["is_end"]:
            break
        print("-----------------------------",timestamp-1," 끝-------------------")
        print()
        # print(action)
        # print(e_id,e_floor,e_status,e_passengers)
        # break


elevator_simulator()