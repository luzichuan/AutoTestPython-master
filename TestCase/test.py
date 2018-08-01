class A:
    def getValue(self):
        return 1

class B:
    def setName(self):
        self.name = 2

class C(A,B):
    def __init__(self):
        self.value = self.getValue()
        self.setName()


test = C()
print test.name
print test.value