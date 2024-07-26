# Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma
# de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se
# o número lido não for maior do que zero, o programa termina com a mensagem “Número
# inválido”
num = input("Digite um numero: ")
texto = str(num)

soma = int(texto[0]) + int(texto[1]) + int(texto[2])

print(f"a soma de todos os numeoros e {soma}")

