class self_test:
    def function1(self):
        print("function1 called")

    def function2(self):
        print(id(self))
        print("function2 called")


f = self_test()
#print(dir(f))

f.function1()
f.function2()