class funcionario:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matri = matricula
        self.sala = salario

class vendedor(funcionario):
    def __init__(self, nome, matricula, salario,bater_ponto:bool):
        super().__init__(nome, matricula, salario)
        self.ponto = bater_ponto

    def comissao(self):
        print(f"{self.nome} comsegui uma comissao de R$ 100,00 reais ")
    
    def bater_meta(self):
        print(f"O vendedor {self.nome} bateu a meta!! ")
              
class gerente(funcionario):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)
        self.senh = senha
    
    def senhas(self):
        print(f"O gerente {self.nome} esqueceu a senha :( ")

        
pessoa1 = vendedor("Carlão do fi perdido","26/07/2024","2.200","14:00")
pessoa2 = gerente("Flavin do pneu","10/07/2024","4.100","123459",)

print(pessoa1.nome)
print(pessoa1.matri)
print(pessoa1.sala)
print(pessoa1.ponto)
pessoa1.bater_meta()
pessoa1.comissao()
print("")
print(pessoa2.nome)
print(pessoa2.matri)
print(pessoa2.sala)
print(pessoa2.senh)
pessoa2.senhas()