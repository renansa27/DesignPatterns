
class Resource:

    """ Método é útil caso a criação das classes abaixo seja um processo complexo"""

    __value = 0

    def reset(self):
        """ 0 = Inicialização padrão """
        self.__value = 0

    def setValue(self, number):
        self.__value = number

    def getValue(self):
        return self.__value


class ObjectPool:
    
    """ Gerenciador de recursos.
    Gerencia saída e retorno de recursos dos clientes.
    Deve ser uma classe singleton.
    """

    __instance = None
    __resources = list()

    def __init__(self):
        if ObjectPool.__instance != None:
            raise NotImplemented("Classe Singleton")

    @staticmethod
    def getInstance():
        if ObjectPool.__instance == None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def getResource(self):
        if len(self.__resources) > 0:
            print ("Usando recurso já existente.")
            return self.__resources.pop(0) 
        else:
            print ("Cria novo recurso")
            return Resource()

    def returnResource(self, resource):
        resource.reset()
        self.__resources.append(resource)

def main():
    pool = ObjectPool.getInstance()

    # Serão criados
    one = pool.getResource()
    two = pool.getResource()

    one.setValue(10)
    two.setValue(20)

    print ("%s = %d" % (one, one.getValue()))
    print ("%s = %d" % (two, two.getValue()))

    pool.returnResource(one)
    pool.returnResource(two)

    one = None
    two = None

    # Recursos sendo reutilizados.
    one = pool.getResource()
    two = pool.getResource()
    print ("%s = %d" % (one, one.getValue()))
    print ("%s = %d" % (two, two.getValue()))


if __name__ == "__main__":
    main()

class Pool: 

    __instance = None
    __unused = list()
    __used = list()
    __max_pool_size = 3

    def __init__(self, max_pool_size=None):
        if Pool.__instance is not None:
            raise NotImplemented('Não deve permitir criar, classe é Singleton')
        Pool.__instance = self
        if max_pool_size is not None:
            Pool.__max_pool_size = max_pool_size

    @staticmethod
    def get_pool_instance(): 
        if Pool.__instance is None:
            Pool.__instance = Pool()
        return Pool.__instance

    def create_new_instance(self, used=True):
        if len(self.__used) + len(self.__used) >= self.__max_pool_size:
            return None
        instance = Resource()
        if used:
            self.__used.append(instance)
        else:
            self.__unused.append(instance)
        return instance

    def get_unused(self):
        if len(self.__unused) > 0:
            i = self.__unused.pop(0)
            self.__used.append(i)
            return i
        else:
            return None

    def return_instance(self, instance):
        if instance in self.__used:
            if instance in self.__unused:
                return False
            self.__unused.append(instance)
            self.__used.remove(instance)
            return True
        else:
            return False

    def get_all_unused(self):
        return self.__unused.copy()

    def get_all_used(self):
        return self.__used.copy()

    def get_number_of_used(self):
        return len(self.__used)

    def get_number_of_unused(self):
        return len(self.__unused)

    def max_pool_size(self):
        return self.__max_pool_size
