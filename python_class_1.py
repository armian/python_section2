class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("----------")
        print("Name: {}".format(self.name))
        print("Phoen: {}".format(self.phone))
        print("----------")

    def __del__(self):
        print("delete!")

user1 = UserInfo("choi", "010-123-4567")
user2 = UserInfo("kim", "010-987-6543")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
