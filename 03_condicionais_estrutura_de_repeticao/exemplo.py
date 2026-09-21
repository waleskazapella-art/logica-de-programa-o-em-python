#1. Estrutura condicionais
from operator import truediv

nota = 6

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
        print("recuperação")
else:
    print("Reprovado")

# 2. condições com operadores logicos
#and -> todas condições devem ser verdadeiras
#or -> pelo menos uma verdadeira
#not -> inverte

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada permitida")
else:
    print("Entrada não permitida")

# 3. Estrutura De Repetição

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

#for
for numero in range (1,6):
    print(numero)

# 5. Percorrendo uma lista
nomes = ["Ana", "Carlos", "João", "Maria"]

for nome in nomes:
    print(nome)

#6 break

#0 break nterrompe

for numero in range(1,11):
    if(numero) == 6
        break

    print(numero)

# 7. condição dentro da repetição

for numero in range(1,11):

    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")