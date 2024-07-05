# Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas
# (as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede dois
# valores numéricos e realiza a operação, mostrando o resultado e finalizando o programa.

print("escolha uma das opcoes abaixo:")
print("1: Soma")
print("2: Sub")
print("3: Multi")
print("4: Divi")

operacao = input("Escolha a operacao (1/2/3/4)!: ")

if operacao in ['1', '2', '3', '4']:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    if operacao == '1':
        print(f"Resultado:",num1 + num2)
    elif operacao == '2':
        print(f"Resultado:",num1 - num2)
    elif operacao == '3':
        print(f"Resultado:",num1 * num2)
    elif operacao == '4':
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("isso e impossivel!!!!!!!")
else:
    print("Opcao invalida tente dnv!!")