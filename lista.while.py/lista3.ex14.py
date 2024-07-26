# Crie um programa que leia um número inteiro positivo par N e imprima todos os números 
# pares de 0 até N em ordem crescente.


N = int(input("Digite um numero: "))

if N > 0 and N % 2 == 0:
    for i in range(0, N + 1, 2):
        print(i)
else:
    print("o numero escolhido nao e par, nao e inteiro ou nao e positivo >:(")
