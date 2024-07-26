# Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de 
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente 
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação

notas = []
while True:
    nota = float(input("Digite uma nota: "))
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        break

media = sum(notas) / len(notas) if notas else 0
print(f"A media das notas e {media}")