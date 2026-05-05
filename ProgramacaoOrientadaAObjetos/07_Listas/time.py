class time:
    def __init__(self, id, nome, estado):
        self.set_id(id)
        self.set_nome(nome)
        self.set_estado(estado)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")  
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")  
        self.__nome = nome
    def set_email(self, estado):
        self.__estado = estado
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__estado
    def __str__(self):
        return f"Seu id {self.__id}\n Seu nome {self.__nome}\n Seu estado {self.__estado}"

class jogador:
    def __init__(self, id, nome, ncamisa, idtime, time):
        self.set_id(id)
        self.set_nome(nome)
        self.set_ncamisa(ncamisa)
        self.set_idtime(idtime)
        self.set_time(time)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")  
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")  
        self.__nome = nome
    def set_email(self, ncamisa):
        self.__ncamisa = ncamisa
    def set_email(self, idtime):
        self.__idtime = idtime
    def set_email(self, time):
        self.__time = time
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_estado(self):
        return self.__ncamisa
    def get_estado(self):
        return self.__idtime
    def get_estado(self):
        return self.__time
    def __str__(self):
        return f"Seu id {self.__id}\n Seu nome {self.__nome}\n Id do seu time {self.__idtime}\n Número da sua camisa{self.__ncamisa}\n Time que você joga {self.__time}"

class FutUI:
    fut = []   # atributo de classe - é uma lista de contatos
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = FutUI.menu()
            if op == 1: FutUI.inserir()   # C reate
            if op == 2: FutUI.listar()    # R ead
            if op == 3: FutUI.atualizar() # U pdate
            if op == 4: FutUI.excluir()   # D elete
            if op == 5: FutUI.pesquisar()
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Fim")
        return int(input("Escolha um opção: "))
    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        x = fut(id, nome, email, fone)
        cls.contatos.append(x)
        print("Contato inserido com sucesso")      
    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print("Nenhum contato na agenda")
        else:
            for x in cls.contatos: print(x)    
    @classmethod
    def listar_id(cls, id):
        # procurar um contato na lista com o id informado
        for x in cls.contatos:
            if x.get_id() == id: return x
        return None    
    @classmethod
    def atualizar(cls):
        FutUI.listar()
        id = int(input("Informe o id do contato a ser alterado: "))
        x = FutUI.listar_id(id)
        if x != None:
            # remove o contato atual
            cls.contatos.remove(x)
            # insere um novo contato com os dados atualizados
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo telefone: ")
            x = fut(id, nome, email, fone)
            cls.contatos.append(x)            
    @classmethod
    def excluir(cls):
        FutUI.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        x = FutUI.listar_id(id)
        if x != None:
            # remove o contato atual
            cls.contatos.remove(x)