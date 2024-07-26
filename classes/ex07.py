class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self._nome = nome
        self._cor = cor
        self._tamanho = tamanho
        self._preco = preco

    def queroBrincar(self):
        return print(f"Estou brincando com o {self._nome}, da cor {self._cor}, do tamanho {self._tamanho}, do preco R${self._preco}")
    
class Carrinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
class Joaninha(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Lego(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Boneca(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Tabuleiro(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class jogoDaVelha(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class quebraCabeca(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class videoGame(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Piao(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)

class Estilingue(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco):
        super().__init__(nome, cor, tamanho, preco)
    
if __name__ == "__main__":
    car = Carrinho("Hot Wheels","Vermelho","20 cm",20.00)
    joa = Joaninha("Rafaela","Vermelha e com bolinhas pretas","5 mm",1.50)
    le = Lego("McLaren Senna","Prata","50 cm",347.99)
    bon = Boneca("Phernelophy","Branca","1.11 m",599.99)
    tab = Tabuleiro("Tabuleiro fodastico","Preto e Rosa","20 cm",34.49)
    jogo = jogoDaVelha("Jogo da velha fodastico 2","Branco com linhas pretas","10 cm",24.99)
    quebra = quebraCabeca("Quebra cabeça fodastico","Cores fodasticas","30 cm",499.99)
    video = videoGame("Xbox Series X","Preto","50 cm",5344.99)
    pia = Piao("Piao Fodasticamente foda","Marrom com listras laranjas","20 cm",5.99)
    est = Estilingue("Estilambo","Marrom","20 cm",20.00)

car.queroBrincar()
print()
joa.queroBrincar()
print()
le.queroBrincar()
print()
bon.queroBrincar()
print()
tab.queroBrincar()
print()
jogo.queroBrincar()
print()
quebra.queroBrincar()
print()
video.queroBrincar()
print()
pia.queroBrincar()
print()
est.queroBrincar()