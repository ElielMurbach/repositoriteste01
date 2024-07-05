# Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários
# acima de R$ 2500,00. Dado o número de horas trabalhadas por um funcionário, informar o valor
# do seu salário líquido.

horas = int(input("Digite as suas horas de trabalho: "))
salario = horas * 40.50

if salario > 2500:
    
    sala_liq=salario-salario*0.11

    print(f"O seu salario normal e {salario}!")
    print(f"O seu salario liquido e {sala_liq}!")

else:
    print(f"Seu salario sem desconto e {salario}")
    

    