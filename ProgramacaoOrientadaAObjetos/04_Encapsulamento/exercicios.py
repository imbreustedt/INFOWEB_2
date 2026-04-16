# Entidade
class Triangulo:
    def __init__(self):
        self.__b = 0.0
        self.__h = 0.0
    def set_base(self, v):
        if v >= 0:              self.__b = v
        else:                   raise ValueError()
    def set_altura(self, v):
        if v >= 0:              self.__h = v
        else:                   raise ValueError()
    def get_base(self):         return self.__b
    def get_altura(self):       return self.__h
    def calc_area(self):        return self.__b * self.__h / 2

class Circulo:
    def __init__(self):
        self.__raio = 0.0
    def set_raio(self, v):
        if v >= 0:                  self.__raio = v
        else:                       raise ValueError()
    def get_raio(self):             return self.__raio
    def calc_area(self):            return (self.__raio ** 2) * 3.14
    def calc_circunferencia(self):  return self.__raio * 3.14 * 2
    
class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0
    def set_distancia(self, v):
        if v >= 0:              self.__distancia = v
        else:                   raise ValueError()
    def set_tempo(self, v):
        if v >= 0:              self.__tempo = v
        else:                   raise ValueError()
    def get_distancia(self):    return self.__distancia
    def get_tempo(self):        return self.__tempo
    def calc_velocidade(self):  return self.__distancia / self.__tempo
    
class Banco():
    def __init__(self):
        self.__titular = ""
        self.__nconta = 0
        self.__saldo = 0.0
    def set_titular(self, t):  self.__titular = t
    def set_nconta(self, nc):  self.__nconta = nc
    def set_saldo(self, s):    self.__saldo = s
    def get_titular(self):     return self.__titular
    def get_nconta(self):      return self.__nconta
    def get_saldo(self):       return self.__saldo
    #Operações Bancárias:
    def deposito(self, valor):
        if valor > 0:           self.__saldo += valor
        else:                   raise ValueError()
    def saque(self, valor):
        if valor > 0:           self.__saldo -= valor
        else:                   raise ValueError()

class Cinema():
    def __init__(self):
        self.__dia = ""
        self.__horario = 0
    def set_dia(self, d):
        dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        if d.lower() in dias:   self.__dia = d.lower()
        else:                           raise ValueError()
    def get_dia(self):                  return self.__dia
    def set_horario(self, h):
        if 0 <= h <= 23:      self.__horario = h
        else:                 raise ValueError()
    def get_horario(self):            return self.__horario
    def calcular_inteira(self):
        if self.__dia == "quarta":    return 8.0
        if self.__dia in ["segunda", "terça", "quinta"]:   valor = 16.0
        else:
            valor = 20.0
        if self.__horario >= 17:
            valor *= 1.5    
        return valor
    def calcular_meia(self):
        if self.__dia == "quarta":
            return 8.0
        return self.calcular_inteira() / 2


# Interface com usuário (User Interface) - prints, inputs
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.triangulo()
            if op == 2: UI.circulo()
            if op == 3: UI.viagem()
            if op == 4: UI.banco()
            if op == 5: UI.ingresso()

    @staticmethod
    def menu():
        print("1-Triângulo 2-Círculo 3-Viagem 4-Conta Bancária 5-Ingresso 9-Fim")
        op = int(input("Informe uma opção: "))
        return op    

    @staticmethod
    def triangulo():
        print("Cálculo da área do triângulo")
        x = Triangulo()
        x.set_base(float(input("Informe o valor da base: ")))     # método de instância
        x.set_altura(float(input("Informe o valor da altura: ")))
        area = x.calc_area()
        print(f"Um triângulo com base {x.get_base()} e altura {x.get_altura()} tem área = {area}")

    @staticmethod
    def circulo():
        x = Circulo()
        x.set_raio(float(input('Informe o valor do raio: ')))
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        print(f"Um circulo com raio {x.get_raio()} tem circunferência = {circunferencia} tem área = {area}")

    @staticmethod
    def viagem():
        x = Viagem()
        x.set_distancia(float(input('Informe a distância que você percorreu: ')))
        x.set_tempo(float(input('Informe o tempo que você levou: ')))
        velocidade = x.calc_velocidade()
        print(f"A Velocidade Média no tempo de {x.get_tempo()} e na distância de {x.get_distancia()} é de {velocidade}")

    @staticmethod
    def banco():
        x = Banco()
        x.set_titular(input('Diga o nome do titular da conta: '))
        x.set_nconta(input('Diga o número da sua conta: '))
        x.set_saldo(float(input('Diga o saldo na sua conta: ')))
        x.deposito(float(input('Diga o valor do seu depósito: ')))
        print(f"O titular da conta é {x.get_titular()}, com número de conta = a {x.get_nconta()} e saldo de {x.get_saldo()}")
        x.saque(float(input('Quanto você quer sacar? ')))
        print(f"Operação realizada. Saldo final: R$ {x.get_saldo():.2f}")

    @staticmethod
    def ingresso():
        x = Cinema()
        x.set_dia(input("Informe o dia da semana: "))
        x.set_horario(int(input("Informe o horário da sessão: ")))
        inteira = x.calcular_inteira()
        meia = x.calcular_meia()
        print(f"Sessão: {x.get_dia().capitalize()} às {x.get_horario()}h")
        print(f"Valor Inteira: R$ {inteira:.2f}")
        print(f"Valor Meia: R$ {meia:.2f}")

UI.main()