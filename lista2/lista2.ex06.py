# Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou V Vespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso

periodo = str(input("Digite o seu periodo de escola: "))

if (periodo == "M"):
    print("Bom Dia!")

elif (periodo == "V"):
    print("Boa Tarde!")

elif (periodo == "N"):
    print("Boa Noite!")