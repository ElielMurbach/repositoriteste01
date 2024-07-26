# Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser 
# informado o número de dados lidos e número de valores pares. O processo termina quando for 
# digitado o número 0



numeros_lidos = 0
numeros_pares = 0

while True:
    numero = int(input("Digite um numero:  "))
    if numero == 0:
        break
    numeros_lidos += 1  
    if numero % 2 == 0:
        numeros_pares += 1
print(f"Numero de dados {numeros_lidos}")
print(f"Numero de valores {numeros_pares}")