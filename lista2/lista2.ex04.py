# Crie um programa que receba três números e mostre-os se estão em ordem crescente

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if (num1 < num2 < num3):
    print("E ordem crescente!")
else:
    print("E ordem decrescente!")