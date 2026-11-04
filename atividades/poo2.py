class Veiculo:
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ligado =
False
    def ligar(self):
        self.ligado = True
        print(f"{self.marca} {self.modelo} está ligado")

    def mostrar_info(self):
        print(f"{self.marca} {self.modelo}, Ligado: {self.ligado}")


veiculo1 = Veiculo('Ford', 'Mustang', False)
veiculo2 = Veiculo('Honda', 'Civic', False)


veiculo1.ligar()


veiculo1.mostrar_info()
veiculo2.mostrar_info()


class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado)
        self.portas = portas


    def abrir_porta_malas(self):
        print(f"O porta-malas foi aberto.")


carro = Carro('Ford', 'Ka', False, 4)
carro.ligar()
carro.mostrar_info()
carro.abrir_porta_malas()


class Moto(Veiculo):
    def __init__(self, marca, modelo, ligado, cilindradas):
        super().__init__(marca, modelo, ligado)
        self.cilindradas = cilindradas
    def empinar(self):
        if self.ligado == False:
            print(f"A moto está desligada, não é possível empinar.")
        else:
            print(f"Vrum vrum")


moto1 = Moto('marca genérica', 'modelo genérico', False, 346)
moto1.mostrar_info()
moto1.ligar()
moto1.mostrar_info()


class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome