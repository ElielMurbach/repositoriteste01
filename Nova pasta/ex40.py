sb = float(input("Digite o valor do salário-base:"))
imposto = (sb*0.07)
grat = (sb*0.05)
total = sb-imposto+grat
print("O funcionário receberá:",total)
