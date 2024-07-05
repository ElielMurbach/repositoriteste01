# Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo, se
# forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# • O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
# • Chama-se equilátero o triângulo que tem três lados iguais.
# • Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# • Recebe o nome de escaleno o triângulo que tem os três lados diferentes.


lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

lados = [lado1,lado2,lado3]


if lados[0] + lados[1] >= lados[2]:
    print("Este triangulo e valido")
    if (lados[0] == lados[1] or lados[1] == lados[2]) and not(lados[0] == lados[1] == lados[2]):
        print("O triangulo e isoceles")
    elif lados[0] == lados[1] == lados[2]:
        print("O triangulo e equilatero")
    else:
        print("O triangulo e escaleno")
else:
    print("esse triangulo nao existe :/")