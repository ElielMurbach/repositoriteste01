# A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
# aprovado. Crie todas as verificações necessárias.

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1) + (nota2) + (nota3) / 3

if media >= 6:
    print("Parabems voce foi aprovado!! ")
    print(f"Sua media foi {media:.1f}!")

if media >= 0 and media < 3:
    print("Infelismente voce ficou de recuperaçao")
    print(f"Sua media foi de {media}")

else:
    print("aprovado")
