class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print(id(self))
        print("function2 called!")


f = SelfTest()

#print(dir(f))

print(id(f))
f.function2()
print(SelfTest.function1())
