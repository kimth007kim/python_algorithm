import requests
import json
from collections import deque
from pprint import pprint


url = "http://localhost:8000"
state={
    "token":"",
    "timestamp":0,
    "elevators":[],
    "is_end":False
}
calls=[]
picked=[]
requestCount=0


def start_API(problem,elevator_cnt):
    global state
    res= requests.post(url+f'/start/KIM/{problem}/{elevator_cnt}')
    state= res.json()
    print("TOKEN: ",state["token"])


def oncall_API():
    global state
    global calls
    headers={"X-Auth-Token":state["token"]}
    res= requests.get(url+"/oncalls",headers={"X-Auth-Token":state["token"]})
    state= res.json()
    calls=state["calls"]
    print("state ======",state)
    print("calls ======",calls)
    print()

def action(commands):
    global state
    headers= {"X-Auth-Token":state["token"],"Content-Type":"application/json"}
    res= requests.post(url+"/action",headers=headers,data=json.dumps({"commands":commands}))
    state=res.json()
    oncall_API()
    global requestCount
    requestCount+=2
    pprint(commands)

def makeCommand(elevator_id,command,ids=None):
    ret = {"elevator_id":elevator_id,"command":command}
    print(ret)
    if ids:
        ret["call_ids"]=ids
    return ret


class Elevator:
    def __init__(self,elevator_id,topFloor,bottomFloor,capacity):
        self.elevator_id = elevator_id
        self.topFloor=topFloor
        self.bottomFloor=bottomFloor
        self.capacity=capacity
        self.toUp=True
        self.el =None
        self.renewElevatorState()
    def renewElevatorState(self):
        global state
        self.el=state["elevators"][self.elevator_id]
    def getNextActions(self):
        self.renewElevatorState()
        ret = []

        getOff_ids=[]
        for passenger in self.el["passengers"]:
            print("지금 들어와계신 승객분",passenger)


        getIn_ids=[]
        global calls
        global picked
        print("picked====",picked)
        for call in calls:
            # print("콜을 부르신 승객분들",call)
            if call["start"]==self.el["floor"] and call["id"] not in picked:
                getIn_ids.append(call["id"])
                print("---getIn_ids---",getIn_ids)

        if len(getIn_ids)>0 or len(getOff_ids)>0:
            ret.append(["STOP",None])
            ret.append(["OPEN",None])

            if len(getOff_ids)>0:
                ret.append(["EXIT",getOff_ids])

            left = self.capacity - len(self.el["passengers"])+len(getOff_ids)
            if len(getIn_ids)>0 and left>0:
                ret.append(["ENTER",getIn_ids[:left]])
                picked+=getIn_ids[:left]

            ret.append(["CLOSE",None])

        direction="UP" if self.toUp else "DOWN"
        ret.append(["STOP", None])
        return ret
start_API(0,1)
elevators=[]
elevators.append(Elevator(elevator_id=0,bottomFloor=1,topFloor=5,capacity=8))

actionQ = [[]]
print("STATE",  state)
# print(token)

seq=0
while seq<10:
    print()
    print("현재 들어온 콜입니다!!!!!!",calls)
    print()


    commands=[]
    for el,q in zip(elevators,actionQ):
        if len(q)==0:
            q+=el.getNextActions()
        print("q에들 어온것들!",q)
        command,ids=q.pop(0)
        print("COMMAND, ID:",command,ids)
        commands.append(makeCommand(el.elevator_id,command,ids))
    action(commands)
    seq+=1