import random
def adivinhar():
    num_aleatório = random.randint(0, 101)
    while True:
        num = int(input("Tente acertar o número escolhido entre 0 e 100: "))
        diferenca = num_aleatório - num

        if num == num_aleatório:
            print("Acertou!")
            break
        elif abs(diferenca) <= 5:
            print("Está muito perto.")
        elif abs(diferenca) <= 10:
            print("Está perto.")
        elif abs(diferenca) <= 20:
            print("Não tão perto.")
        elif abs(diferenca) <= 40:
            print("Está longe.")
        elif abs(diferenca) > 40:
            print("Está muito longe.")
            

adivinhar()
