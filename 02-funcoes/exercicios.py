#EX 1
def suce_ante(numero):
    sucessor = numero + 1
    antecessor = numero - 1
    return antecessor, sucessor

print(suce_ante(10))
print(suce_ante(23))

#EX 2
def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

print(media(2, 4, 5))
print(media(6, 8, 3))


#EX 3
def calc_desconto(valor):
    valor_final = desconto = 0
    if 0.1 <= valor <= 0.99:
        desconto = 0
        valor_final = valor
    elif 10 <= valor <= 99.99:
        desconto = 5
        valor_final = valor - (valor * desconto / 100)
    elif 100 <= valor <= 499.99:
        desconto = 10
        valor_final = valor - (valor * desconto / 100)
    elif valor >= 500:
        desconto = 15
        valor_final = valor - (valor * desconto / 100)

    return valor_final, desconto
    
print(calc_desconto(499.99))
print(calc_desconto(300))


#EX 4 e 5
def verificador(codigo):
    valido = False
    invalido = True
    if codigo[0:2].isalpha() and codigo[0:2].isupper() and codigo[2:6].isnumeric() and codigo[-1] == 'X':
        valido = True
        invalido = False
    return valido, invalido

print(verificador('SP408863X'))


#EX 6
def aquario(comprimento, largura, altura, temperaturaAmbiente, temperaturaDesejada):
    volume = (comprimento * altura * largura) / 1000
    potenciaTermostato  = (volume*0.05*(temperaturaAmbiente-temperaturaDesejada))
    filtragemPorHora = volume * 3

    return volume, potenciaTermostato, filtragemPorHora

print(aquario(10, 10, 10, 30, 23))


#EX 7
def main():
    print("Altura:(m)")
    altura = float(input())
    
    print("Peso:(kg)")
    peso = float(input())

    imc = calcular_imc(peso, altura)
    print("Seu IMC é", imc)

    if imc < 18.5:
        print("Você está abaixo do peso normal")
        peso_ideal = calcular_peso_ideal(18.5, altura)
        peso_para_ganhar = peso_ideal - peso
        print("Para chegar ao peso ideal, você precisa ganhar {:.2f} kg".format(peso_para_ganhar))

    elif 18.5 <= imc < 25:
        print("Você está com o peso normal")

    else:
        if 25 <= imc <= 29.9:
            print("Você está acima do peso normal")
        elif 30 <= imc <= 34.9:
            print("Você pertence ao grupo Obesidade de Classe 1")
        elif 35 <= imc <= 39.9:
            print("Você pertence ao grupo de Obesidade Classe 2")
        elif imc >= 40:
            print("Você pertence ao grupo de Obesidade Classe 3")

        peso_ideal = calcular_peso_ideal(24.9, altura)
        peso_para_perder = peso - peso_ideal
        print("Para chegar ao normal, você precisa perder:", peso_para_perder)

def calcular_imc(peso, altura):
    return peso / (altura * altura)

def calcular_peso_ideal(imc_ideal, altura):
    return imc_ideal * (altura * altura)

if __name__ == "__main__":
    main()
