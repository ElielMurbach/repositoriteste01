# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

print("Digite 10 numeros inteiros >:) :")

lista = []

while len(lista) < 10:
    numero = int(input(f"Digite o numero: "))
    lista.append(numero)

menor = min(lista)
maior = max(lista)

print(f"o menor numero e  {menor} B) ")
print(f"o menor numero e {maior} B) ")