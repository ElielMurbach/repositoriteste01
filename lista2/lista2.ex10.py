# Crie um programa que leia um número inteiro e, caso ele seja positivo, calcule e mostre:
# • O número digitado ao quadrado;
# • A raiz quadrada do número digitado;

num = int(input("Digite um numero: "))

if (num >= 0):
    res1 = num ** 2
    res2 = num ** 0.5
    print(f"o numero elevado ao quadrado e {num}*{num} ")
    print(f"a resposta e {res1}")
    print(f"a raiz do numero e {res2:.2f}")

else:
    print("numero invalido!")