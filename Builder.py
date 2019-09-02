class Director:
   __builder = None
   
   def setBuilder(self, builder):
      self.__builder = builder
   
   def getCarro(self):
      carro = Carro()
      
      # Carroceria
      carroceria = self.__builder.getCarroceria()
      carro.setCarroceria(carroceria)
      
      # Motor
      motor = self.__builder.getMotor()
      carro.setMotor(motor)
      
      # Adiciona quatro Pneus
      i = 0
      while i < 4:
         pneu = self.__builder.getPneu()
         carro.setPneu(pneu)
         i += 1
      return carro

# Produto
class Carro:
   def __init__(self):
      self.__pneu = list()
      self.__motor = None
      self.__carroceria = None

   def setCarroceria(self, carroceria):
      self.__carroceria = carroceria

   def setPneu(self, pneu):
      self.__pneu.append(pneu)

   def setMotor(self, motor):
      self.__motor = motor

   def printCarro(self):
      print "Carroceria: %s" % self.__carroceria.tipoCarroceria
      print "Cavalos do motor: %d" % self.__motor.cavalos
      print "Tamanho do aro: %d\'" % self.__pneu[0].tamanhoAro
      print "Quantidade de pneus: %d " % len(self.__pneu)

class Builder:
      def getPneu(self): pass
      def getMotor(self): pass
      def getCarroceria(self): pass

class JeepBuilder(Builder):
   
   def getPneu(self):
      pneu = Pneu()
      pneu.tamanhoAro = 22
      return pneu
   
   def getMotor(self):
      motor = Motor()
      motor.cavalos = 170
      return motor
   
   def getCarroceria(self):
      carroceria = Carroceria()
      carroceria.tipoCarroceria = "SUV"
      return carroceria

# Partes do Carro
class Pneu:
   tamanhoAro = None

class Motor:
   cavalos = None

class Carroceria:
   tipoCarroceria = None

def main():
   jeepBuilder = JeepBuilder() # Inicializando a classe
   
   director = Director()
   
   # Montando o Jeep
   print "Jeep"
   director.setBuilder(jeepBuilder)
   jeep = director.getCarro()
   jeep.printCarro()

main()