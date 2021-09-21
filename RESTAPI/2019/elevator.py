import requests


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
    command='[]'
    tmp= requests.get(uri, headers={"X-Auth-Token": token}, data= {"commands":cmd})
    return tmp.json()
def p0_simulator():
    user = 'tester'
    problem = 1
    count = 2

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))
    oncall_res = onCall(token)
    while True:
        oncall_res=onCall(token)
        origin_calls = oncall_res["calls"]
        elevators = oncall_res["elevators"]
        print(origin_calls,elevators)
        # print(oncall_res)
        act= action(token,{'elevator_id': "1", 'command': 'OPEN'})
        print(act)
        break



if __name__ == '__main__':
    p0_simulator()