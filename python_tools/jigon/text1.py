class test:
    def  __init__(self,a =10,b=12):
        self.a = a
        self.b = b
    def jia(self):
        return self.a + self.b
    def jian(self):
        return self.a - self.b


if __name__ == '__main__':
    t = test(20,33)
    print(t.jia(self=10,))
    t1 = test(10, 20)
    print(t1.jian())