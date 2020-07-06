class Common:
    def process(self):
        print("Process in Common")


class A(Common):
    pass


class B(Common):
    def process(self):
        print("Process in B")


class C(A, B):
    pass


obj = C()
obj.process()
print(C.mro())
