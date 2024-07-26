# Crie um programa que leia dois números. Após a leitura, inverta o valor delas e mostre as mesmas
# com os valores invertidos.

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero:"))

num3 = num1 - num1 + num2
num4 = num2 - num2 + num1

print (f"primeiro que era {num1} vira {num3} e o segundo era {num2} vira {num4}")