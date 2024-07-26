i = 0
soma = 0

while i < 10:
    try:
        num = int(input("Digite um numero: "))
        soma += num
        i = i + 1
    except:
        print("Entrada invalida meo Deos Abensoado....")
        print("-"*8)
    
print("total:",soma)