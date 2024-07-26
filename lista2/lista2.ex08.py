# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
# número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

num = float(input("Digite um numero: "))

if (num >= 0):
    res = num ** 2
    print(res)
else:
    print ("numero invalido!")
