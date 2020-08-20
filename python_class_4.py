class NameTest:
    total = 0

print(dir())
print("before : ", NameTest.__dict__)

NameTest.total = 1

print("after  : ", NameTest.__dict__)

n1 = NameTest()
n2 = NameTest()

print(id(n1), " vs ", id(n2))

print(dir())

print(n1.__dict__)
print(n2.__dict__)

n1.total = 77
print(n1.__dict__)

print(n1.total)
print(n2.total)

n1.next = 100
print(n1.next)
