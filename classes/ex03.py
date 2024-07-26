class ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco (self,preconovo):
         self.preco = preconovo
         print("O preço foi alterado! ")
    
    def mostrar_setor(self):
        print(f"seu setor é o {self.setor}")

class IngressoVip(ingresso):
    def __init__(self, preco:int, setor:str, camarote:bool, open_bar:bool, open_food:bool, estacionamento:bool):
        super().__init__(preco, setor)
        self.cama = camarote
        self.op_bar = open_bar
        self.op_food = open_food
        self.estacio = estacionamento

    def camarote(self):
        if self.cama == True:
            print("voce tem camarote!")
        else:
            print("voce nao tem camarote!! ")

    def bebidas(self):
        if self.op_bar == True:
            print("Você tem direito a bebida! ")
        else:
            print("Você nao tem direito a bebidas! ")
    
    def comida(self):
        if self.op_food == True:
            print("Você tem direito a comida a vontade! ")
        else:
            print("Você nao tem direito a comida")
    
    def estacionamento(self):
        if self.estacio == True:
            print("Voce tem direito a estacionamento gratis!! ")
        else:
            print("voce nao tem direito a estacionamento, tera que pagar!! ")

ingresso1 = ingresso("R$ 70","arquibancada")
ingressoVip1 = IngressoVip("R$ 140","Cruzeiro do Neymar",True,True,True,False)

print(ingresso1.preco)
print(ingresso1.setor)
ingresso1.alterar_preco("R$ 60")
print(ingresso1.preco)
print("")
print(ingressoVip1.preco)
print(ingressoVip1.setor)
ingressoVip1.camarote()
ingressoVip1.bebidas()
ingressoVip1.comida()
ingressoVip1.estacionamento()