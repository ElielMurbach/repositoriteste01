# Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor
# de sua aquisição: Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser
# vendido por um preço 45% maior, caso contrário o lucro será de 30%. Sabendo disso, Crie um
# algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda

preco_aquisicao = float(input("Digite o valor de aquisicao do produto: "))

if preco_aquisicao < 50.00:
    preco_venda = preco_aquisicao * 1.45
else:
    preco_venda = preco_aquisicao * 1.30

print(f"O valor de venda do produto é {preco_venda}")