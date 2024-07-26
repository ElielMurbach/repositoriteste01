# O gestor de uma rede de shoppings, precisa contratar um sistema para 
# administrar o estacionamento, a principal função do sistema é calcular
# Tempo(). Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora
# adicional. O principal 
# argumento da função é o tempo utilizado em minutos, a função deve 
# retornar o valor total. Caso o usuário fique no estacionamento por
# menos de 15 minutos, o tempo utilizado não será cobrado.​

def hora(min_tempo):
    if min_tempo < 15:
        return 0.0
    hora_ficada = min_tempo + 59 // 60
    if hora_ficada == 1:
        return 9.0
    else:
        return 9.0 + hora_ficada - 1 * 1.5

print(hora(10))    
print(hora(90))   
print(hora(120))  
print(hora(150))  
