class Automobile:
    def __init__(self,__make,__model,__mileage,__price):
        self.__make=__make
        self.__model=__model
        self.__mileage=__mileage
        self.__price=__price

    def set_make(self):
        self.__make=input()
    def set_model(self):
        self.__model=input()
    def set_mileage(self):
        self.__mileage=input()
    def set_price(self):
        self.__price=input()
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price
