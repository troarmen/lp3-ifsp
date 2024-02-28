#Tipos de dados

# Numérico

# int
idade = 10

# float
altura = 1.65

# Booleano
# True, False
verdade = True
mentira = False


# str = string
# seq de caracteres
# literal de str
nome = "José"
nome = 'José'

#multilinhas
frase = """ 
Parev
Inchbes ek
Husam lav ek
Getse Hay Heghapokhagan Tashnagtsutyune!
"""

#interpolação de string
nome = "Sonia"
idade = 23
mensagem = f"Olá {nome}. Você tem {idade} anos"
print(nome[0])

#str são objetos
# métodos
print(nome.upper())
print(nome)

# list
# lista de valores
# pode conter valores de tipos diferentes
# podem ser alteradas(adicionar, remover)
habilidade = ["java", "html", "css", True, 10.2]
print(habilidade[0])
habilidade[0] = "o que eu quiser" 
habilidade.append("python")

# adicionar em uma posição
habilidade.insert(0, "Kotlin")
print(habilidade)
# remove, sort, clear, copy...

for habilidad in habilidade:
    print(habilidad)

# tuple
# lista de valores 
# não pode alterar os valores
opcoes = ("sim", "não", "talvez")
racas_rpg = ("anao", "humano", "elfo")
print(opcoes[1])


# funcao que retorna estatisticas 
# sobre as notas de um aluno
# media, maior nota, menor nota
# entrada: n1, n2, n3 ou notas(list)
def estatistica_nota(notas):
    media = sum(notas) / len(notas)
    menor = min(notas)
    maior = max(notas)
    return media, menor, maior

notas = [10.0, 5.5, 3.2, 1.8]
estatistica = estatistica_nota(notas)
print(estatistica)

# desempacotamento
media, menor, maior = estatistica_nota(notas)

# set
# conjunto de valores
# não permite valores duplicados
# não é indexado
habilidades = {'java', 'python', 'css'}
habilidades.add('assembly')
print(habilidades)

# dicionario
# palavra (key)
# definição (value)
pessoa = {
    'Nome':'Silvio Santos', 
    'Casado':True,
    'idade': 20
}
print(pessoa['Nome'])
pessoa['rico'] = True
print(pessoa)


# None
# null
nulo = None