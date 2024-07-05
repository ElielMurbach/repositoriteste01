# . Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite a idade: "))
contri = int(input("Digite o tempo de contribuição: "))

if idade >= 65:
    print("pode aposentar aposentar")
elif contri >= 30: 
    print("pode a ponsentar aposentar")
elif idade >= 30 and contri >= 25:
    print("pode se aposentar")
else:
    print("Nao pode se aposentar")