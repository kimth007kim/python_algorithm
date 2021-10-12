from collections import deque
import sys

input = sys.stdin.readline


n,k  = map(int,input().split())
data = list(map(int,input().split()))

def finish(k,belt):
    cnt=0
    for i in belt:
        # print(belt[i].durability)
        if belt[i].durability<=0:
            cnt+=1
    # print(cnt)
    if cnt>=k:
        return False
    else:
        return True

class slot:
    def __init__(self,number,durability):
        self.number = number
        self.durability = durability
        self.robot =-1
    def __str__(self):
        return "번호는: {} , 내구도는: {} 로봇:{} ".format(self.number, self.durability,self.robot)

belt={}
for i in range(1,n*2+1):
    belt[i]=slot(i,data[i-1])
for i in belt:
    print(belt[i])

time = 1
product=1
now = [i for i in range(1,n+1)]
print(now)
# for i in belt:
#     print(i,belt[i])

while True:

    # 1단계 벨트 회전하기
    # 현재 위에 나와있는 벨트

    for i in range(len(now)):
        now[i]=now[i]-1
        if now[i]==0:
            now[i]=n*2
    # print("1번 후의 now", now)

    print("1단계",now)
    # print("1단계", n-1,belt[now[n-1]])

    # 맨마지막 벨트면 제외시키기
    if belt[now[n-1]].robot>0:
        # print("1단계의 제외 해당")
        belt[now[n-1]].robot=-1
    # print("{}단계의 {}번 진행완료 ".format(time, 1))

    # 2단계 가장먼저 올라간 로봇부터 한칸 이동할수 있다면 이동 ,아니면 가만
    arr=[]
    for i in range(len(now)-1):
        if belt[now[i]].robot>0:
            arr.append([belt[now[i]].robot,now[i]])
    if len(arr)>0:
        arr.sort(key = lambda x:x[0])
        q=deque(arr)
        while q:
            # print("q에 있는 것들",q)
            order, num=q.popleft()
            if num==n*2:
                next=1
            else:
                next=num+1
            # print(num,"---->",next)
            if belt[next].durability>0 and belt[next].robot==-1:
                tmp=belt[num].robot
                belt[next].robot=tmp
                belt[next].durability-=1
                belt[num].robot=-1
                if next ==now[n-1]:
                    belt[next].robot=-1
    # print("{}단계의 {}번 진행완료 ".format(time, 2))


    # 3단계 올리는 위치에 있는 칸의 내구도가 0이아니면 올리는 위치에 로봇을 올림
    # 올리는 칸 now[0]
    if belt[now[0]].durability>0 and belt[now[0]].robot==-1:

        belt[now[0]].robot=product
        belt[now[0]].durability-=1
        product+=1
    #     print("{}번에  로봇{} 번 을 올리고 내구도:{} 로 감수완료".format(belt[now[0]].number,belt[now[0]].robot , belt[now[0]].durability))
    # print("{}단계의 {}번 진행완료 ".format(time, 3))

    # 4단계 내구도 0인칸의 개수가 K개이상이라면 종료
    if not finish(k,belt):
        break

    # print("{}단계의 {}번 진행완료 ".format(time, 4))
    time+=1

# print("끝나는 시각",time)
print(time)