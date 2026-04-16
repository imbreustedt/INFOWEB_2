class pais:
    def dados(self):
        self.nome = 0
        self.populacao = 0
        self.area = 0
    def am2(self):
        return self.populacao / self.area

x = pais() 
x.nome = input('Diga o nome do pais:\n')
x.populacao = float(input('Diga o numero da populacao\n'))
x.area = float(input('Diga a area:\n'))
print(x.populacao, x.area)
y = x.am2()
print(f"A densidade demográfica do {x.nome} é {y:.2f} hab/km²")