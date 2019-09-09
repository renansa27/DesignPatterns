from abc import ABCMeta, abstractmethod

class Tema(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def color(self):
        pass


class DarkTheme(Tema):

    def color(self):
        return 'Preto'


class LightTheme(Tema):

    def color(self):
        return 'Azul Claro'


class AquaTheme(Tema):

    def color(self):
        return 'Cinza Claro'


class WebPage(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def content(self):
        pass


class About(WebPage):

    def __init__(self, tema):
        self.__tema = tema

    def content(self):
        return 'About page in {}'.format(self.__tema.color())


class Home(WebPage):

    def __init__(self, tema):
        self.__tema = tema

    def content(self):
        return 'Home page in {}'.format(self.__tema.color())


if __name__ == '__main__':
    dark_tema = DarkTheme()
    aqua_tema = AquaTheme()

    about = About(dark_tema)
    home = Home(aqua_tema)

    print(about.content())
    print(home.content())