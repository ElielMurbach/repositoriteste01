# 5 – Escreva um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas. Por fim deve retornar o novo valor para o usuário considerando o percentual do imposto.​

def somaImposto(taxaImposto, custo):
    novo_valor = custo + (custo * (taxaImposto / 100))
    return novo_valor


taxa = 10 
custo_item = 100  

novo_valor = somaImposto(taxa, custo_item)
print(f'O novo valor e {taxa}%, E R${novo_valor:.4f}')