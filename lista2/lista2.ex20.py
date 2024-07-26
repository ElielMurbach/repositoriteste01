# Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno
# foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

media = (nota1 + nota2 + (nota3 * 2)) / 4

if media >= 60:
    print("Parabems voce foi aprovado!! ")
    print(f"Sua media foi {media:.1f}!")
else:
    print("REPROVADO!!!")
