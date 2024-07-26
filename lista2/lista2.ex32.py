# Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes
# categorias:
# Categoria Idade
# Infantil 5 a 12
# Juvenil 12 a 17
# Sênior maiores de 18 anos

idade = int(input("Digite a sua idade: "))


if idade < 12:
    print("criança!")
elif idade < 18: 
    print("jovem!")
else:
    print("veio!")