# . Crie um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela
# a média destas notas. Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0,
# onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o
# programa termina.

nota1 = float(input("Digite a primeira nota: "))


if (nota1 >= 0 and nota1 <= 10 ):
    
    nota2 = float(input("Digite a segunda nota: "))

    if (nota2 >= 0 and nota2 <= 10):

        media = (nota1+nota2)/2
        print (f"A sua media e {media}")
    else:
        print("Nota 2 invalida!")
else:
    print("Nota 1 invalida!")
    
    
    