class Fridge:
    def __init__(self):
        self.isOpened=False
        self.foods=[]

    def open(self):
        self.isOpened=True
        print('냉장고 문이 열리다!')

    def put(self,thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어갔네..')
        else:
            print('냊앙고 문이 닫혀있어서 못넣겠어요..')
    def close(self):
        self.isOpened=False
        print("냉장고 문을 닫았습니다.")
class Food:
    pass
f= Fridge()
apple=Food()
elephant = Food()
f.open()
f.put(elephant)
# print(f.open())
