# and
# todas precisam ser verdadeiras
from operator import truediv

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)

# or
#pelo menos uma

idade = 16
acompanhado = True

resultado = idade >= 18 or acompanhado
print(resultado)

#not; inverte

aluno_matriculado = True
print(not aluno_matriculado)

#2  comparação

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

#3 . ESTRUTURA if

idade = 18

if idade >= 18:
    print("Maior de idade")

#4 . if / else

idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")