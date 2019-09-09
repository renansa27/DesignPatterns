from abc import ABCMeta, abstractmethod

class Tema(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def cor(self):
        pass


class TemaEscuro(Tema):

    def cor(self):
        return 'Preto'


class TemaClaro(Tema):

    def cor(self):
        return 'Azul Claro'


class TemaColorido(Tema):

    def cor(self):
        return 'Colorido'


class PaginaWeb(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def content(self):
        pass


class Ajuda(PaginaWeb):

    def __init__(self, tema):
        self.__tema = tema

    def content(self):
        return 'A página Ajuda está com o tema {}'.format(self.__tema.cor())


class Home(PaginaWeb):

    def __init__(self, tema):
        self.__tema = tema

    def content(self):
        return 'A página Home está com o tema {}'.format(self.__tema.cor())


if __name__ == '__main__':
    temaEscuro = TemaEscuro()
    temaColorido = TemaColorido()

    ajuda = Ajuda(temaEscuro)
    home = Home(temaColorido)

    print(ajuda.content())
    print(home.content())