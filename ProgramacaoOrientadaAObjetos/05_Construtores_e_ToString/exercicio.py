class Retangulo:
    def __init__(self, b, h):
        self.__b = 0
        self.__h = 0
        if b >=0:               self.__b = b
        else:                   raise ValueError()
        if h >= 0:              self.__h = h
        else:                   raise ValueError()
    def set_base(self, v):
        if v >=0:               self.__b = v
        else:                   raise ValueError()
    def set_altura(self, v):
        if v >=0:               self.__h = v
        else:                   raise ValueError()
    def get_base(self):         return self.__base
    def get_altura(self):       return self.__altura
    def __str__(self):          return f"Base = {self.get_base()}, Altura = {self.get_altura()}"
    def calc_area(self):        return self.__b * self.__h
    def calc_diagonal(self):    return ((self.__b ** 2) + (self.__h ** 2) ** 0.5)