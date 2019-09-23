class FiguraGeometrica:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def getBase(self):
        return self.base

    def getAltura(self):
        return self.altura

    def calculaAreaRetangulo(self):
        return self.base * self.altura

    def calculaAreaTriangulo(self):
        return (self.base * self.altura ) / 2


class Retangulo:

    retangulo = FiguraGeometrica(2,10)

    print('Retangulo')
    print(retangulo.getBase())
    print(retangulo.getAltura())
    print(retangulo.calculaAreaRetangulo())

class Triangulo():

    triangulo = FiguraGeometrica(10,2)

    print('Triangulo')
    print(triangulo.getBase())
    print(triangulo.getAltura())
    print(triangulo.calculaAreaTriangulo())


if  __name__ == " __main__ ":
    Retangulo()
    Triangulo()