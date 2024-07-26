# Considerando o intervalo de 0 a 100. Crie um programa que calcule e mostre a soma dos 50 
# primeiros números pares.

soma = 0
contador = 0
numero = 0

while contador < 51:
    if numero % 2 == 0:
        soma += numero
        contador += 1
    numero += 1

print(f"A soma dos numeros e {soma}")