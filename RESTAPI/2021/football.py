class player:
    def Shoot(self):
        print("goal입니다!")
    def setData(self,name,score,country,position,height):
        self.name= name
        self.score=score
        self.country=country
        self.position=position
        self.height=height

    def printData(self):
        print("이름:",self.name)
        print("포지션:",self.position)

    def __init__(self):
        print("객체가 생성되었다!")
Kim = player()
Kim.setData('손흥민',98,'korea','공격수',181)
Kim.Shoot()
Kim.printData()

# print(Kim)