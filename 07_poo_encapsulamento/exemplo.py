#1. Encapsulamento
#proteger o salario para que so mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R${self.salario}")

#@property deixa ler o salario como se fosse atributo
@property
def salario(self):
    return self.__salario
def dar_aumento(self, porcentagem):
    if porcentagem <= 0:
        print(f"Aumento invalido para {self.nome}")
        return
    self.__salario = self.__salario * (1 + porcentagem / 100)
    print(f"{self.nome} recebeu {porcentagem}% de aumento")

######

ana = Funcionario("Ana", 3000)
ana.salario = 4000
print(ana.salario)
ana.apresentar()

#alterar erro
try:
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salario diretamente")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario não pode ser acessado fora.")