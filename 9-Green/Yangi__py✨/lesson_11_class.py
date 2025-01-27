""" Class """
""" OOP - object oriented programming"""

class Car():
    """ OOP - object oriented"""
    def __init__(self, company:str, model:str,color:str,price:int, year:int):
        self.company = company
        self.model = model
        self.color = color
        self.price = price
        self.year = year

    def show_info(self):
        """ Show information about"""
        info  = f" About car \nCompany:{self.company}, Model: {self.model}, Color: {self.color}, Price: {self.price}, Year: {self.year}"
        return info


car1 = Car("tesla","model 2","white",300_333333, 2025)
car2 = Car("BMW","M5","BLACK",300_333333, 2025)

print(car1.show_info())
print(car2.show_info())


""" obyekt hususiyat va metodlar ko'rish"""
"""   dir() function """
from pprint import pprint

print(dir(Car))
# print(dir(Book))


""" __dict__ metodi"""
"""__dct__ metodi obyektni xususiyatlarini luhgat korinishida qaytaradi"""
# pprint(h.__dict__)
pprint(car1.__dict__)
pprint(car2.__dict__)









