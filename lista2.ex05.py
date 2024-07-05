# Crie um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva:
# F - Feminino, M – Masculino ou Sexo Inválido.

gene = str(input("Digite seu genero: "))

if (gene == "F" or gene =="f"):
    print("Feminino") 
elif(gene == "M" or gene == "m"):
       print("Masculino")
else:
    print("Sexo invalido!")
    