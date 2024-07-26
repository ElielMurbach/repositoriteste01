# Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem
# crescente. Caso contrário, imprima não está em ordem crescente.

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))

if (num1 < num2 < num3):
    print("esta em ordem crescente!")
else:
    print("nao esta em ordem crescente!")