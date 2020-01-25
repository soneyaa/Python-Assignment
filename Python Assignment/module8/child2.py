from automobile import Automobile
class Truck(Automobile):
    def __init__(self,__make,__model,__mileage,__price,__drive):
        Automobile.__init__(self,__make,__model,__mileage,__price)
        self.__drive=__drive
    def set_drive(self):
        self.__drive=input()
    def get_drive(self):
        return self.__drive
def main():
    c=Truck(1897,'eureka','25kmpl',500000,2)
    print(c.get_drive())

main()
