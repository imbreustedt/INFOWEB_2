class Bingo:
    def __init__(self, numbolas, bolas):
        self.set_numbolas(numbolas) = 0
        self.set_bolas(bolas) = 0
    def set_numbolas(self, numbolas):
        self.__numbolas = numbolas
    def set_numbolas(self, bolas):
        self.__bolas = bolas
    def get_numbolas(self): return self.__numbolas
    def get_bolas(self): return self.__bolas   
    def __str__(self):
        return f"{self.__numbolas} - {self.__bolas}"

class BingoUI:
    contatos = []   # atributo de classe - é uma lista de contatos
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = BingoUI.menu()
            if op == 1: BingoUI.inserir()   # C reate
            if op == 2: BingoUI.listar()    # R ead
            if op == 3: BingoUI.atualizar() # U pdate
            if op == 4: BingoUI.excluir()   # D elete
    @staticmethod
    def menu():
        print("1-Iniciar Novo Jogo | 2-Sortear Número | 3-Verificar Números | 4-Fim")
        return int(input("Escolha um opção: "))
    @classmethod
    def IJ():

ContatoUI.main()