def lista():
    print("Loja quase dois - Tabale de preços")
    Y=1.99
    X=1
    for linha in range(50):
        print(f"{X} - R$ {Y:.2f}")
        Y+=1.99
        X+=1
lista()