# Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um
# percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
# Consumo (Km/l) Mensagem
# menor que 8 Venda o carro!
# entre 8 e 14 Econômico!
# maior que 12 Super econômico!


gasolina = float(input("Digite a gasolina comsumida: "))
quilometro = float(input("Digite a quilometragem andada com a gasolina: "))

kmComLitro = quilometro / gasolina

if kmComLitro < 8:
    print(f"o carro faz {kmComLitro:.1f}km com 1 litro,Opala VEIO!")
elif kmComLitro < 14: 
    print(f"o carro faz {kmComLitro:.1f}km com 1 litro,e bem economico")
else:
    print(f"o carro faz {kmComLitro:.1f}km com 1 litro,parabems muito economico")