class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0.0
        self.__combustivel = 0.0
    def set_destino(self, d):
        if d.strip() != "": self.__destino = d
        else: raise ValueError()
    def set_distancia(self, v):
        if v > 0: self.__distancia = v
        else: raise ValueError()
    def set_combustivel(self, v):
        if v > 0: self.__combustivel = v
        else: raise ValueError()
    def get_destino(self):     return self.__destino
    def get_distancia(self):   return self.__distancia
    def get_combustivel(self): return self.__combustivel
    def consumo(self):
        return self.__distancia / self.__combustivel
    def __str__(self):
        return f"Destino: {self.__destino} | Distância: {self.__distancia}km | Litros: {self.__combustivel}L"
class ViagemUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = ViagemUI.menu()
            if op == 1: ViagemUI.calculo()
            if op == 2: print("Fim.")

    @staticmethod
    def menu():
        print("\n1 – Calcular  2 – Fim")
        op = int(input("Informe uma opção: "))
        return op

    @staticmethod
    def calculo():
        x = Viagem()
        x.set_destino(input("Informe o destino: "))
        x.set_distancia(float(input("Informe a distância (km): ")))
        x.set_combustivel(float(input("Informe o combustível (L): ")))
        print(x.__str__())
        print(f"Consumo médio: {x.consumo():.2f} km/l")

ViagemUI.main()