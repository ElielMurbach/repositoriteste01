# 10 – Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento. Ela tem uma quantia X para dar de entrada,
# uma taxa de juros é definida pelo banco e a pessoa pode escolher o número de parcelas que deseja financiar. ​

# Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos. O programa deve solicitar ao usuário o valor do veiculo,
# o valor da entrada, a taxa de juros e a quantidade de parcelas. Além disso, o programa deve exibir o valor total pago,
# a quantia dos juros pagos e o valor de cada parcela. O programa deve apresentar as informações de forma clara e objetiva, facilitando a compreensão por parte do usuário.​


def financeiro():
    
    valor_veiculo = float(input("Digite o valor do veiculo: "))
    valor_entrada = float(input("Digite o valor da entrada: "))
    taxa_juros_anual = float(input("Digite a taxa de juros: ")) / 100
    num_parcelas = int(input("Digite as parcelas: "))
    valor_financiado = valor_veiculo - valor_entrada
    taxa_juros_mensal = (1 + taxa_juros_anual) ** (1 / 12) - 1
    valor_parcela = valor_financiado * (taxa_juros_mensal * (1 + taxa_juros_mensal) ** num_parcelas) / ((1 + taxa_juros_mensal) ** num_parcelas - 1)
    valor_total_pago = valor_parcela * num_parcelas
    juros_pagos = valor_total_pago - valor_financiado
    
    print("\n----- Resultado da Simulação -----")
    print(f"Valor do veiculo: R$ {valor_veiculo:.2f}")
    print(f"Valor da entrada: R$ {valor_entrada:.2f}")
    print(f"Valor financiado: R$ {valor_financiado:.2f}")
    print(f"Taxa de juros mensal: {taxa_juros_mensal * 100:.2f}%")
    print(f"Quantidade de parcelas: {num_parcelas}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
    print(f"Valor total pago: R$ {valor_total_pago:.2f}")
    print(f"Juros pagos: R$ {juros_pagos:.2f}")

financeiro()