'''Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o est
abelecido pelo regulamento de pesca do MS (50 Kg) deve pagar uma multa de R$ 4,00 por quilo excedente. O pescador precisa que você crie uma função p
ara ler a quantidade de peixes e calcular o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da
 multa que o pescador deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

def controle(excesso,multa,peixe,peso):
    
    return excesso,multa,peixe,peso

peso = float(input("Digite o peso do peixe: "))
peixe = int(input("Digite a quantidade de peixe: "))

excesso = peso * peixe
if excesso > 50:
    excesso = excesso - 50
    multa = excesso * 4.00
    print(f"Você passou {excesso} KG")
    print(f"Sua multa será de R${multa}")
else:
    print("Limite não excedido")
