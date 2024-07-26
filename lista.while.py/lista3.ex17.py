# Escreva um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros 
# números naturais.

n = int(input("Digite um numero: "))

if n > 0:
    soma = n * (n + 1) // 2
    print (f"A soma dos {n} primeiros numeros naturais e: {soma}")
else:
    print("numero invalido, burro >:(")