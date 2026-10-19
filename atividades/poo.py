class Cachorro:

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

cachorro1 = Cachorro("Belinha", "poodle", "2 meses")
cachorro2 = Cachorro("Auau", "Borzoi", "1 ano")

cachorro2.idade = "5 meses"
print(cachorro2.idade)

def latir(self):
    print(f"{self.nome} diz auau")
def mostrar_info(self):
    print(self.nome, self.idade, self.raca)

latir(cachorro2)

mostrar_info(cachorro2)