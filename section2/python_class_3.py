#클래스 변수, 인스턴스 변수

class Warehouse:
    stock_num = 0

    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse("Kim")
user2 = Warehouse("Han")

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__) #인스턴스 네임스페이스 먼저 확인후 class 네임스페이스 확인, class 변수(공유)
print(user1.stock_num)
print(user2.stock_num)