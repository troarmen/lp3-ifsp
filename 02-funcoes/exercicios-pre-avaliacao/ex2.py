def tabuada():
    num = int(input("Digite um número para ver sua tabuada: "))
    for c in range(0, 11):
        print(f"{num} x {c} = {num * c}")


tabuada()