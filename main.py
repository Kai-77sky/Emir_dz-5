
import re


class ValidCarNumber:

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        isvalid = re.search(r"0[1-9](KG|RU|KZ)([0-9]{3})([A-Z]{3})", self.number)
        try:
            if isvalid.end() == len(self.number):
                print("Валидный номер!")
            else:
                print("Невалидный номер!")
        except:
            print("Невалидный номер!")


num = ValidCarNumber(input("Введите номер машины: "))
num.is_valid()