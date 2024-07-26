# Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente
# a este número. Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

dia = int(input("Digite o numero: "))

if dia == 1:
    print("Domingou!!")
elif dia == 2:
    print("Segundou!!")
elif dia == 3:
    print("Terçou!!")
elif dia == 4:
    print("Quartou!!")
elif dia == 5:
    print("Qintou!!")
elif dia == 6:
    print("SEXTOU!!")
elif dia == 7:
    print("Sabadou!!")

else:
    print("Dia da semana invalido :/")


