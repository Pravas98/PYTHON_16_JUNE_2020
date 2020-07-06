class A:
    def process(self):
        print("Process in A")
        self.show()

    def show(self):
        print("Show in A")


class B:
    def process(self):
        print("Process in B")


class C(A, B):
    def process(self):
        A.process(self)
        B.process(self)

    def show(self):
        print("Show in C")


obj = A()
obj.process()

obj = C()
obj.process()
