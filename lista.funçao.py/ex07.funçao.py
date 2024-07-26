def calcular_salario(horas_trabalhadas, salario_base):
    valor_hora_normal = salario_base / 40
    
    if horas_trabalhadas <= 40:
        salario_total = horas_trabalhadas * valor_hora_normal
    else:
        horas_extras = horas_trabalhadas - 40
        valor_hora_extra = valor_hora_normal * 1.5
        salario_total = (40 * valor_hora_normal) + (horas_extras * valor_hora_extra)
    
    return salario_total


horas_trabalhadas = 40
salario_base = 2000  

salario_a_pagar = calcular_salario(horas_trabalhadas, salario_base)
print(f"O salario a ser dado e: R${salario_a_pagar:.2f}")