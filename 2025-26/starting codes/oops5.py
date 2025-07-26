class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Class started")


    @staticmethod
    def stop():
        print("Class stopped")


class toyota(car):
    def __init__(self,brand,type):
        self.brand=brand
        super().__init__(type)

car1=toyota("abcd","efg")
print(car1.type)