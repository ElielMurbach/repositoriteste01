# Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e
# escreva o preço novo, e escreva uma mensagem em função do preço novo (de acordo com a
# segunda tabela).
# Preço antigo Percentual de aumento
# até R$ 50 5%
# entre R$ 50 e R$ 100 10%
# acima de R$ 100 15%

valor = float(input("Digite o valor velho: "))

if valor < 50:
    print(f"O valor novo e de R${valor * 1.05:.2f}")
elif valor < 100:
    print(f"O valor novo e de R${valor * 1.10:.2f}")
else: 
    print(f"O valor novo e de R${valor * 1.15:.2f}")