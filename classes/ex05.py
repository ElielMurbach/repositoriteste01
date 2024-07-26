class pessoa:
    def __init__(self,nome,telefone,Email,endereço):
        self.nome = nome
        self.tele = telefone
        self.email = Email
        self.endere = endereço

class fisica(pessoa):
    def __init__(self, nome, telefone, Email, endereço,cpf):
        super().__init__(nome, telefone, Email, endereço)
        self.cpf = cpf

    def fugir(self):
        print(f"{self.nome} esta fugindo do lula!! ")
              
class juridica(pessoa):
    def __init__(self, nome, telefone, Email, endereço,cnpj):
        super().__init__(nome, telefone, Email, endereço)
        self.cnpj = cnpj

    def prender(self):
        print(f"{self.nome} esta mandando prender o Carlão do fi perdido por apoiar o bolsonaro >:( ")

pessoa1 = fisica("Carlão do fi perdido","67-9666-6666","CarlãodofiPerdido@gmail.com","Rua Tchurusbangos Thurusbagos",13847194)
pessoa2 = juridica("Flavin do pneu","67-99999-9999","Flavindopneu@gmail.com","Rua Tomar!",33749174943)

print(pessoa1.nome)
print(pessoa1.tele)
print(pessoa1.email)
print(pessoa1.endere)
print(pessoa1.cpf)
pessoa1.fugir()
print("")
print(pessoa2.nome)
print(pessoa2.tele)
print(pessoa2.email)
print(pessoa2.endere)
print(pessoa2.cnpj)
pessoa2.prender()