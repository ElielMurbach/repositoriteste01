class pessoa:
    def __init__(self, matricula,nome,idade):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

class professor(pessoa):
    def __init__(self, matricula,nome,idade,formaçao,diciplina,carga_horaria,salario):
        super().__init__(matricula, nome, idade)
        self.form = formaçao
        self.dici = diciplina
        self.ch = carga_horaria
        self.sala = salario

    def em_aula(self):
        print(f"professor{self.nome} esta ensinando {self.diciplina} WoW! ")


    def calcu_salari(self):
        salario_anual = self.sala * 12
        return salario_anual

class aluno(pessoa):
    def __init__(self, matricula, nome, idade, notas):
        super().__init__(matricula,nome,idade)
        self.nota = notas

    def calcu_medi(self):
        if self.nota:
            media = sum(self.nota) / len(self.nota)
            return media
        else:
            return 0
    
    def estudar(self):
        print(f"o aluno {self.nome} esta estudando! ")

    
aluno1 = aluno("100E","Eliel",16,[8,9,6,10,6])
professor1 = professor("WOW9","clebinho",46,"Quimica quantica","Quimica",12,4000)

print(aluno1.nome)
print("")  
print(aluno1.idade)
print("")
print(aluno1.matricula)
print("")
print(aluno1.nota)
print("")
aluno1.estudar()
print("")
print(aluno1.calcu_medi())


print("")
print("----------------------------")
print("")

print(professor1.nome)
print("")
print(professor1.idade)
print("")
print(professor1.form)
print("")
print(professor1.ch)
print("")
print(professor1.sala)
print("")
print(professor1.dici)
print("")
print(professor1.calcu_salari())