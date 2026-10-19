#A CLASSE: 0 modelo(a planta)
from types import coroutine


class Celular:

    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#OS Objetos: Criados a partir da classe (as "casas)
celular1 = Celular("Samsung", "galaxy s23", "Preto")
celular2 = Celular("Motorola", "MotoG", "azul", 30)

#acessando e alterando atributos
print(celular2.marca)

#Tambem podemos alterar diretamente
celular1.cor = "Branco"
print(celular1.cor)

#chamando metodos
celular2.ligar()