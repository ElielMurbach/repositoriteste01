# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
# não for válido, mostrar uma mensagem de erro


valor = float(input("Digite o valor do produto: "))
estado = input("Digite o Estado: ")


if estado == "MG" or estado == "mg":
    print(f"O valor final é de R${valor * 1.07:.2f}")
elif estado == "SP" or estado == "sp":
    print(f"O valor final é de R${valor * 1.12:.2f}")
elif estado == "RJ" or estado == "rj":
    print(f"O valor final é de R${valor * 1.15:.2f}")
elif estado == "MS" or estado == "ms":
    print(f"O valor final é de R${valor * 1.08:.2f}")
else:
    print("O valor e invalido")