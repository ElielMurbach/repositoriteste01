numero_provas = int(input("Digite quantas privas voce fez: "))
i = 0
soma = 0
while i < numero_provas:
    soma += float(input("Digite a suas notas: "))
    i = i + 1
media = soma / numero_provas

print (f"Sua media foi de {media}")

#---------------------------------------------------