class triangulo:
    def __init__(self):
        self.b = 0  #atributo de base (nesse caso)
        self.h = 0  #atributo de altura (nesse caso)
    def calc_area(self):
        return self.b * self.h / 2

#o x    é uma referencia que armazena o endereço de um objeto
#trinagulo() crai um objeto (ou instancia) da classe
x = triangulo() 
print(x.b, x.h)
x.b = float(input('Informe a base de um triangulo\n'))
x.h = float(input('Informe a altura de um triangulo\n'))
print(x.b, x.h)
a = x.calc_area()
print(f"A area do triangulo é {a:.2f}")