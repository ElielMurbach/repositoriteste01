# Escreva um programa que leia um número inteiro positivo ímpar N e imprima todos os 
# números ímpares de 1 até N em ordem crescente.


N = int(input("Digite um numero: "))

if N > 0 and N % 2 != 0:
    for i in range(1, N + 1, 2):
        print(i)
else:
    print("o numero nao e inpar, positivo ou inteiro >:(")