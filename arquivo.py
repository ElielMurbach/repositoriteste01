class filme:

    def __init__(self,nome,duraçao):
        self._nome = nome
        self._duraçao = duraçao

    def play(self):
        print(f"o filme {self._nome} esta sendo exibido! ")


class aventura(filme):
    def __init__(self, nome, duraçao):
        super().__init__(nome, duraçao)

    def tesouro(self):
        print("WOOOOOW")

class comedia(filme):
    def __init__(self, nome, duraçao):
        super().__init__(nome, duraçao)
    
    def risadas(self):
        print("ajbfuiabeuifbyuiavefyuvayvfyawyga")

class terror(filme):
    def __init__(self, nome, duraçao):
        super().__init__(nome, duraçao)

    def grito(self):
        print("OMG um fantasma AAAAAAAAAAAAAAAAAAA")

class musical(filme):
    def __init__(self, nome, duraçao):
        super().__init__(nome, duraçao)

    def Horrivel(self):
        print("Q filme Orrivel mds ksksks")



filmAventura = aventura("Uncharted",230)
filmComedia = comedia("SuperBad",160)
filmTerror = terror("o iluminado",210)
filmMusical = musical("Minecraft o filme",666)

print("-----------------------------")

filmAventura.play()
filmAventura.tesouro()

print("-----------------------------")

filmComedia.play()
filmComedia.risadas()

print("-----------------------------")

filmTerror.play()
filmTerror.grito()

print("-----------------------------")

filmMusical.play()
filmMusical.Horrivel()

print("-----------------------------")

