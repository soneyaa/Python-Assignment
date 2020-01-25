from automobile import Automobile
class Car(Automobile):
    def __init__(self,__make,__model,__mileage,__price,__doors):
        Automobile.__init__(self,__make,__model,__mileage,__price)
        self.__doors=__doors
    def set_doors(self):
        self.__doors=input()
    def get_doors(self):
        return self.__doors
def main():
    c=Car(1897,'eureka','25kmpl',500000,4)
    print(c.get_doors())
    print(c.get_make())
    print(c.get_model())
    print(c.get_mileage())
    print(c.get_price())
    c.set_doors()
    c.set_make()
    c.set_model()
    c.set_mileage()
    c.set_price()
    print(c.get_doors())
    print(c.get_make())
    print(c.get_model())
    print(c.get_mileage())
    print(c.get_price())
main()

