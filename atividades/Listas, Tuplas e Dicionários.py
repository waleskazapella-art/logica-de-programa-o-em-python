#1. Criar uma lista contendo inicialmente 5 filmes.
#2. Exibir todos os filmes cadastrados.
#3. Exibir o primeiro filme da lista.
#4. Exibir o último filme da lista.
#5. Adicionar um novo filme ao final da lista.
#6. Inserir um novo filme em uma posição específica.
#7. Remover um filme da lista.
#8. Alterar o nome de um dos filmes.
#9. Exibir a quantidade de filmes cadastrados.
#10. Verificar se um determinado filme está presente na lista.
from selectors import SelectSelector

nomes = ["Megatubarão", "Titanic 666", "The mortuary assistent", "Obsession", "Creep"]
print(nomes)

print(nomes[0])

print(nomes[-1])

nomes.append("SCREAMBOAT")
print(nomes)

nomes.insert(2, "A substancia")
print(nomes)

nomes.remove("The mortuary assistent")
print(nomes)

nomes[0] = "Sobrenatural"
print(nomes)

print(len(nomes))

if "Creep" in nomes:
    print("Creep está na lista")
else:
    print("Creep não está na lista")

print("//////////////////////")

#1. Criar uma lista contendo 5 notas.
#2. Exibir todas as notas.
#3. Calcular a soma das notas.
#4. Calcular a média das notas.
#5. Identificar a maior nota.
#6. Identificar a menor nota.
#7. Verificar se existe uma nota igual a 10.
#8. Informar se o estudante foi aprovado ou reprovado.
#9. Considerar média igual ou superior a 7 como aprovação.

#1 e 2
notas = [6, 4.5, 7.4, 9, 8]
print(notas)

#3
soma = notas[0]+notas[1]+notas[2]+notas[3]+notas[4]
print(soma)

#4
media = soma/5
print(media)

#5

notaMaior = 0
for nota in notas:
    if nota > notaMaior:
        notaMaior = nota
print(notaMaior)

#6

notaMenor = 100000
for nota in notas:
    if nota < notaMenor:
        notaMenor = nota
print(notaMenor)

#7
if 10 in notas:
    print("Existe uma nota 10 na lista.")
else:
    print("Não existe uma nota 10 na lista.")

#8

if media >= 7:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")
#9

print("//////////////////////")

#1.
info = ("Arroz", "alimento", 20, 545654566)
print(info[0])
print(info[1])
print(info[2])
print(info[3])

#2.
print("\n=== INFORMAÇÕES PRODUTOS ===")
for item in info:
    print(item)

#3
print("\n=== QUANTIDADE INFO ===")
print(len(info))

#4.
temp = list(info)
temp[2] = 4000
info = tuple(temp)
print(info)

print("//////////////////////")

#4. Cadastro de funcionário

#1.
funcionario = {
    "Nome": "fulano",
    "Idade": 21,
    "Cargo": "estoquista",
    "Salário": 3000,
    "Setor": "estoque",
}

print(funcionario)

#2.

funcionario["Salário"] = "5000"
print(funcionario)

#3.
funcionario["Anos de Experiência"] = 2
print(funcionario)

#4.
del funcionario["Idade"]
print(funcionario)

#5.
if "Setor" in funcionario:
    print("O dicionário possui a chave Setor.")
else:
    print("O dicionário não possui a chave Setor.")

#6.
for chave in funcionario:
    print(chave, funcionario[chave])

print("⊹₊˚‧︵‿₊⊱·✶·⊰₊‿︵‧˚₊⊹")

#5. Sistema de estoque

#1.
produtos = [
    {"Nome": "Celular", "Categoria": "Eletrônico", "Preço": 3000, "Quantidade": 10},
    {"Nome": "Laptop", "Categoria": "Eletrônico", "Preço": 5000, "Quantidade": 5},
    {"Nome": "Teclado", "Categoria": "Periférico", "Preço": 300, "Quantidade": 15},
    {"Nome": "Mouse", "Categoria": "Periférico", "Preço": 200, "Quantidade": 20},
    {"Nome": "Mousepad", "Categoria": "Acessório", "Preço": 80, "Quantidade": 30}
]

print("=== PRODUTOS DISPONÍVEIS ===")
print("\nCelular")
print("Laptop")
print("Teclado")
print("Mouse")
print("Mousepad")

#2.
print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

#3.
soma = 0
for produto in produtos:
    soma += produto["Quantidade"]
print("\nQuantidade total do estoque:", soma)

#4.
preco = 0
for produto in produtos:
    preco += produto["Preço"]
print("Preço do estoque:", preco)

#5.
for produto in produtos:
    if produto["Quantidade"] < 10:
        print(f"\nO produto {produto['Nome']} está com baixo estoque.\n ")

#6.
if "Celular" not in produtos:
     print("O produto Celular está cadastrado.")

#7.
produtos[1]["Quantidade"] = 7
print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

#8.
novo_cadastro = {"Nome": "Gabinete", "Categoria": "Componente", "Preço": 1500, "Quantidade": 20}
produtos.append(novo_cadastro)

print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])
print("Produto 6:", produtos[5])