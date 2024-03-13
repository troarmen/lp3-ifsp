#Funcao
#Modulariza o programa
#Reuso
#Manutenabilidade

#Declaração
def ola_mundo():
    print('Olá mundo!')

#Chamada
ola_mundo()


#Função sem retorno
#Side effect - Efeito colateral
def imprimir_mensagem(nome):
    print(f'Bom dia {nome}')

imprimir_mensagem('AMENAYN HAYOTS HRAMANADAR KAREKIN NJTEH')

#Função com retorno
#função pura
def mensagem(nome):
    return f'Bom dia {nome}'


#Parâmetros e argumentos
def somar(numero1, numero2):
    return numero1 + numero2

numero = 3

somar(10, numero)
somar(10, somar(3, 5))


#Escopo de variáveis
def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

print(media(10, 3, 4.6))


#Parâmetros com valor padrão
def mensagem(nome, mensagem='Boa noite'):
    return f'{mensagem},{nome}'

mensagem('Marcos', 'Bom dia')
print(mensagem('KAREKIN NJTEH'))

#Argumentos nomeados
print('Parev', '123', 'ports', sep='@')

mensagem(nome='KEVORK TCHAVUSH', mensagem='PAREEEV')
mensagem(mensagem='PARI LUYS', nome='TRASTAMAD GANAYAN')


def media(*notas):
    return sum(notas) / len(notas)

print(media(10.5, 5.5, 7.5))



