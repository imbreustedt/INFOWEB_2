class circulo:
    def __init__(self):
        self.raio = 0
    def calc_circunferencia(self):
        return 2 * self.raio * 3.14
    def calc_area(self):
        return self.raio**2 * 3.14

x = circulo()
x.raio = 5
x.calc_area()
x.calc_circunferencia()