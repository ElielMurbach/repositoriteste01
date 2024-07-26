# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. A 
# quantidade de números a serem lidos deve será fornecida pelo usuário


quantidade = int(input("Digite a quantidade de numeoros: "))

if quantidade > 0:
    maior_numero = int(input("Digite um numero: ")) 

    for i in range(1, quantidade):
        numero = int(input(f"Digite outro numero: "))
        if numero > maior_numero:
            maior_numero = numero
    print(f"O maior numero e {maior_numero}")
else:
    print("numero invalido burro >:)")