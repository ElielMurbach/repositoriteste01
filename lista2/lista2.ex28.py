# Crie um programa de uma calculadora simples com as 4 operações básicas, apresente o menu
# de opções abaixo, leia dois números reais. Em seguida mostre o resultado da operação entre os
# dois números recebidos. Escreva uma mensagem de erro se a opção for inválida.
# Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).


valor1 = float(input("Digite o primeiro valor: "))
operacao = input("O que será feita com esse valor? \n[A,a,S,s,M,m,D,d] ")
valor2 = float(input("Digite segundo valor: "))

if operacao == "A" or operacao == "a":
    print(f"{valor1} + {valor2} = {valor1 + valor2}")
elif operacao == "S" or operacao == "s":
    if valor1 > valor2: 
        print(f"{valor1} - {valor2} = {valor1 - valor2}")
    else: 
        print("primeiro valor é menor que o segundo")
elif operacao == "M" or operacao == "m":
    print(f"{valor1} x {valor2} = {valor1 * valor2}")
elif operacao == "D" or operacao == "a":
    if valor1 * valor2 != 0:
        print(f"{valor1} / {valor2} = {valor1 / valor2}")
    else:
        print("nao e possive dividir po zero burro :)")
else:
    print("Valor invalido")