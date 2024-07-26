# Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
# média.

total1 = 0
total2 = 0

print("Digite 10 numeros inteiros que seja positivo :) :")

while total2 < 10:
    numero = int(input("Digite um numero positivo: "))
    if numero > 0:
        total1 += numero
        total2 += 1
    else:
        print("Numero invalido, Digite outro numero >:( ")

media = total1 / 10

print(f"A media dos numeros e: {media}")