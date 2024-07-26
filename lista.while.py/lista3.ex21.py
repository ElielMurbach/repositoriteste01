# Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numeros: "))

soma_pares = sum(num for num in range
(num1, num2 + 1) if num % 2 == 0)
multiplicacao_impares = 1
for num in range(num1, num2 + 1):
    if num % 2 != 0:
        multiplicacao_impares *= num

print(f"A soma dos numeros pares e {soma_pares}")
print(f"A multiplicaçao dos numeros impares e {multiplicacao_impares}")