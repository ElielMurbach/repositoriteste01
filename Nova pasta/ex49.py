lata = int(input("Digite quantas latas de 350 ml foram compradas:"))
gp = int(input("Digite quantas garrafas de 600 ml foram compradas:"))
gg = int(input("Digite quantas garrafas de 2 l foram compradas:"))
L1 = (lata*350)/1000
L2 = (gp*600)/1000
L3 = gg*2
total = L1+L2+L3
print("Foram comprados",total,"L de refrigerante.")
