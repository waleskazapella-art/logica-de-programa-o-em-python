#o que é uma funçao: bloco de codigo para rezalizar uma certa tarefa(organiza e reutiliza)

#01 Criando (def)

def saudacao():
    print("Olá, seja bem vindo!")

saudacao()

#2 parametro

#permitem enviar informações para a função
def saudacao(nome):
    print(f"ola {nome}")

saudacao("Ana")
saudacao("João")

#3 +1 parametro

def apresentar(nome , idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("joao", 18)

#4 def com calculo

def somar(numero1 , numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10,20)
somar(10 , 90)

#5 retornando um valor
#return devolve um valor para o local onde a função foi chamada.

def somar(n1, n2):
    return n1 + n2

print(somar(10,5))

#6. Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(16))
print(verificarIdade(18))

#7 parametro com valor
def saudacao(nome ="Aluno"):
    print(f"Ola {nome}")

saudacao("joao")
saudacao()

#8 funcao utilizando lista
def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma / len(notas)
notas = [8 , 7 , 9 , 10]
media = calcularMedia(notas)
print(f"media: {media}")

#9 funcoes p organizar programa
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n===== Produto =====")
    print(f"Nome: {nome}")
    print(f"preço: R$ {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)