class passagem:
    def __init__(self,preco,assento,):
        self.preco = preco
        self.assent = assento

    def alterar_preco(self,Novopreco):
        self.preco = Novopreco
        print("Preço alterado! ")
    
    def escolher_assento(self,esco_assento):
        self.assent = esco_assento
        print("Escolha um assento: ")

class PassagemBus(passagem):
    def __init__(self, preco, assento, placa, leito, abastecer:bool):
        super().__init__(preco, assento)
        self.plac = placa
        self.leit = leito
        self.abas = abastecer

    def combustivel(self):
        if self.abas == True:
            print("Voce tera que abastecer! ")
        else:
            print("Tanque cheio! ")

    def placa(self):
        print(f"A placa do seu onibus é {self.plac}")

    def leito(self):
        print(f"O seu leito e o {self.leit}")

        
    
class PassagemAviao(passagem):
    def __init__(self, preco, assento,portaodeembarque,checkin,decolar:bool):
        super().__init__(preco, assento)
        self.PdeEmbar = portaodeembarque
        self.check = checkin
        self.decolar = decolar

    def sair(self):
        if self.decolar == True:
            print("Pode decolar!!")
        else:
            print("Não estamos prontos ainda! ")
    
    def embarque(self):
        print(f"Seu portao de embarque e o {self.PdeEmbar}!")

    def checkin(self):
        print(f"Seu checkin e o {self.check}")
    

onibus1 = PassagemBus("R$ 29,99","A12","EAC-1037","304",True)
aviao1 = PassagemAviao("R$ 1258,34","E34","TRS002","nsei.com",True)

print(onibus1.preco)
print(onibus1.assent)
onibus1.escolher_assento("D14")
print(onibus1.assent)
onibus1.placa()
onibus1.leito()
onibus1.combustivel()
print("")
print(aviao1.preco)
print(aviao1.assent)
aviao1.embarque()
aviao1.checkin()
aviao1.sair()