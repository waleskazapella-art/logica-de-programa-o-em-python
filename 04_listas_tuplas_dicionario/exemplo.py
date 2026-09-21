#listas, Tuplas e dicionarios

# 1. Listas
nomes = ["ana" , "Carlos", "João" , "Maria"]
print(nomes)

# 2. Elementos da lista
print(nomes[0])

#acessar ultimo com -1
print(nomes[-1])

# 3 alternando elementos

nomes[0] = "pedro"
print(nomes)

#4 adicionar elementos

#append () adiciona um elemento no final da lista
nomes.append("lucas")
print(nomes)

#insert() adiciona um elemento em uma posição especifica
nomes.insert(1, "Mariana")
print(nomes)


#5 remove
nomes.remove("João")
print(nomes)

# por indice
nomes.pop(0)
print(nomes)

#6 tamanho da lista

print(len(nomes))

#7 percorre

for nome in nomes:
    print(nome)

#8 se existe

if "Lucas" in nomes:
    print("Lucas está na lista")
else:
    print("Lucas não está na lista")

#9 lista com diferentes tipos de album

dados = ["João", 18, 1.75, True]
print(dados)

#10 lista de numeros
notas = (7.5, 8.0, 6.5, 9.0)

soma =0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media}")


#11 tuplas
#semelhantes ás listas
#tuplas n alteram

coordenadas = (10 , 20)
print(coordenadas)

print(coordenadas[0])

#12. dicionarios
#armazenam em formato chave
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)
