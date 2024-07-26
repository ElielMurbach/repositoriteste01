# Escreva um programa que 
# leia 10 inteiros e imprima sua média.

print("Digite 10 numeros inteiros")

total = 0

for i in range(10):
    numero = int(input(f"Digite o numero: "))
    total += numero

media = total / 10

print(f"A media e: {media}")