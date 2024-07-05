# Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e
# a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a
# cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão
# abaixo:
# Especificação Código Preço
# Hot Dog 100 12.00
# X-Salada 102 18.50
# X-BACON 103 25.50
# X-Burguer 104 17.00
# Suco de Laranja 105 9.50
# Refrigerante 106 6.00

codigo = int(input("Digite o código do lanche: "))
quanti = int(input("Digite a quantidade: "))

if codigo == 100:
    print(f"{quanti} o Hot Dog e R${12 * quanti:.2f}")
elif codigo == 102:
    print(f"{quanti} o X Salada e R${18.5 * quanti:.2f}")
elif codigo == 103:
    print(f"{quanti} o X BACON e R${25.5 * quanti:.2f}")
elif codigo == 104:
    print(f"{quanti} o X Burguer e R${17 * quanti:.2f}")
elif codigo == 105:
    print(f"{quanti} o Suco de Laranja e R${9.5 * quanti:.2f}")
elif codigo == 106:
    print(f"{quanti} o Refrigerante e R${6 * quanti:.2f}")
else:
    print("isto nao existe! :)")
