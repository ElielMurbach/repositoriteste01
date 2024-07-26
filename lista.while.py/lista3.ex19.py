# Escreva um algoritmo que leia um número inteiro entre 100 e 9999 e imprima na saída cada um 
# dos algarismos que compõem o número


numero = int(input("Digite um numero: "))

if 100 <= numero <= 9999:
    for i in str(numero):
        print(i)
else:
    print("O numero n esta entre 100 e 9999, burro >:)")