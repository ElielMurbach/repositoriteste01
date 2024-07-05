trapeMenor = float(input("Digite a base menor: "))
trapeMaior = float(input("Digite a base maior: "))
altura = float(input("Digite a altura: "))

if trapeMaior > 0:
    print("Base aprovada!")
else:
    print("Base reprovada!")

if trapeMenor > 0:
    print("Base menor aprovada!")
else:
    print("Base menor Reprovada!")
    
area = (trapeMaior + trapeMenor) * altura / 2

print(f"A area do trapezio e {area:.2f}!!")
