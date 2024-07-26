# Crie um programa que leia 2 números inteiros
# e 1 real. Calcule e mostre: o produto do primeiro
# com a metade do segundo, a soma do triplodo 
# primeiro com o terceiro. O terceiro número
# digitado ao cubo.


numint1 = int(input("Digite um numero inteiro: "))
numint2 = int(input("Digite o sengundo numero inteiro: "))
numreal = float(input("Digite um numero real: "))

res1 = numint1 * (numint2 / 2)
res2 = (numint1 * 3) + numreal
res3 = numreal ** 3

print (f"Resultado do primeiro e: {res1}")
print (f"Resultado do segundo e: {res2}")
print (f"Resultado do terceiro e: {res3}")