# Escreva um programa que peça ao
# usuário para digitar 10 valores e some-os

lista=[]
i = 0
while i < 10:
    lista.append(float(input("Digite um numero: ")))
    i += 1

print("a soma de tudo e:",sum(lista))
