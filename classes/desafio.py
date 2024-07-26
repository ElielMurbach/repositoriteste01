class forma:
    def __init__(self,nome):
        self.nome = nome


class quadrado(forma):
    def __init__(self, nome,lado):
        super().__init__(nome)
        self.lado = lado
    
    def calculo(self,calculo):
        self.calculo = self.lado * self.lado
        print(f"{calculo}")

    
class circulo(forma):
    def __init__(self, nome,raio):
        super().__init__(nome)
        self. raio = raio

    def calcu_raio(self,calculo2):
        self

