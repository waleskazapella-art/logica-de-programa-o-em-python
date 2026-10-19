#1

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    i = 0
    notas = [i]
    for i in range (0,3):
        notas = float(input("Digite a nota do aluno: "))

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma/len(notas)

media = calcularMedia
print(f"Média {media}")

cadastrar_aluno()
