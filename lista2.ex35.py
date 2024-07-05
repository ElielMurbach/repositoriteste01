# Escreva um programa que, dado o valoror da venda, imprima a comissão que deverá ser paga ao
# vendedor. Para calcular a comissão, considere a tabela abaixo:
# Venda mensal Comissão
# Maior ou igual a R$100.000,00 R$700,00 + 16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00 R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00 R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00 R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00 R$500,00 +14% das vendas
# Menor que R$20.000,00 R$400,00 +14% das vendas

valor = float(input("Digite o valor da venda: "))

if valor < 20000:
    print(f"O valor da comissao e R${400 + valor * 0.14:.3f}")
elif valor < 40000:
     print(f"O valor da comissao e R${500 + valor * 0.14:.3f}")
elif valor < 60000:
    print(f"O valor da comissao e R${550 + valor * 0.14:.3f}")
elif valor < 80000:
    print(f"O valor da comissao e R${600 + valor * 0.14:.3f}")
elif valor < 100000:
    print(f"O valor da comissao e R${650 + valor * 0.14:.3f}")
else:     
    print(f"O valor da comissao e  R${700 + valor * 0.16:.3f}")