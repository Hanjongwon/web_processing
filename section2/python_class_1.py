class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("--------------")
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("--------------")

    def __del__(self):
        print('delete!')


user1 = UserInfo("kim", "010-4213-2134")
user2 = UserInfo("Park", "010-4234-2332")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)
print(user1.phone, user1.name)