class Prato(object):
    def prepararPrato(self):
        self.cortar = Cortar()
        self.cortar.cortarVegetais()

        self.cozinhar = Cozinhar()
        self.cozinhar.cozinharVegetais()

        self.fritar = Fritar()
        self.fritar.fritarVegetais()


class Cortar(object):
    def cortarVegetais(self):
        print("Todos os vegetais foram cortados")


class Cozinhar(object):
    def cozinharVegetais(self):
        print("Todos os vegetais foram cozidos")


class Fritar(object):
    def fritarVegetais(self):
        print("Todos os vegetais foram fritos.")

if __name__ == "__main__":
    prato = Prato()
    prato.prepararPrato()