class Test:
    def __init__(self, data):
        self.data = data

    def getData(self):
        print(f"Some data: {self.data}")

    def firstData(self):
        self.getData()

obj1 = Test(10)
obj1.firstData()

def newGetData(self):
    print("After monkey patching")

Test.getData = newGetData
obj1.firstData()



