class Pais:
    def __init__(self):
        self.__nome = ""
        self.__populacao = 0
        self.__area = 0.0
    def set_nome(self, n):
        if n.strip() != "": self.__nome = n
        else: raise ValueError()
    def set_populacao(self, p):
        if p > 0: self.__populacao = p
        else: raise ValueError()
    def set_area(self, a):
        if a > 0: self.__area = a
        else: raise ValueError()
    def get_nome(self):      return self.__nome
    def get_populacao(self): return self.__populacao
    def get_area(self):      return self.__area
    def densidade(self):
        return self.__populacao / self.__area
    def __str__(self):
        return f"País: {self.__nome} | População: {self.__populacao} hab | Área: {self.__area} km²"
    
class PaisUI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = PaisUI.menu()
            if op == 1: PaisUI.calculo()
            if op == 2: print("Fim.")

    @staticmethod
    def menu():
        print("\n1 – Calcular  2 – Fim")
        op = int(input("Informe uma opção: "))
        return op

    @staticmethod
    def calculo():
        x = Pais()
        x.set_nome(input("Informe o nome do país: "))
        x.set_populacao(int(input("Informe a população: ")))
        x.set_area(float(input("Informe a área em km²: ")))
        print(x.__str__())
        print(f"Densidade Demográfica: {x.densidade():.2f} hab/km²")

PaisUI.main()