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

notas = [6, 4.5, 7.4, 9, 8]
print(notas)

soma = notas[0]+notas[1]+notas[2]+notas[3]+notas[4]
print(soma)

media = soma/5
print(media)

