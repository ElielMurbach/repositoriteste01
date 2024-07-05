# Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim
# como a diferença existente entre ambos.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if (num1 > num2):
    res1 = num1 - num2
    print(f"{num1} e maior que {num2}")
    print(f"a diferença entre eles e de {res1}")

elif (num2 > num1):
    res2 = num2 - num1
    print(f"{num2} e maior que {num1}")
    print(f"a diferença entre os dois e de {res2}")

