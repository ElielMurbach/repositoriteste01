# Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal,
# utilizando as seguintes formulas (onde h corresponde à altura):
# • Homens: (72.7∗ h)−58
# • Mulheres: (62,1∗ h)−44,7


altura = float(input("Digite sua altura: "))
genero = input("Digite o seu genero: ")

if genero == 'M' or genero =='m':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7

print(f"O peso ideal e {peso_ideal:.2f} kg")

