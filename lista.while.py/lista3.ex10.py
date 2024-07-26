# Crie um programa que leia um número inteiro N e depois imprima os N primeiros números
# naturais ímpares.

n = int(input("Digite um numero: "))

print(*range(1,2*n,2))