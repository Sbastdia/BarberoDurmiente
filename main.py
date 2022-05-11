from threading import Thread, Lock, Event
import time, random

mutex = Lock()

#Interval in seconds
intervaloMinCliente = 5
intervaloMaxCliente = 15
duracionMinCorte = 3
duracionMaxCorte = 15

class Barberia:
	clientesEspera = []

	def __init__(self, barbero, numeroSillas):
		self.barbero = barbero
		self.numeroSillas = numeroSillas
		print ('Barbería se inicializa con {0} silla'.format(numeroSillas))
		print ('Intervalo mínimo del cliente {0}'.format(intervaloMinCliente))
		print ('Intervalo máximo del cliente {0}'.format(intervaloMaxCliente))
		print ('Duración mínima del corte {0}'.format(duracionMinCorte))
		print ('Duración máxima del corte {0}'.format(duracionMaxCorte))
		print ('---------------------------------------')

	def abrirTienda(self):
		print ('Barbería está abriendo')
		workingThread = Thread(target = self.barberoATrabajar)
		workingThread.start()

	def barberoATrabajar(self):
		while True:
			mutex.acquire()

			if len(self.clientesEspera) > 0:
				c = self.clientesEspera[0]
				del self.clientesEspera[0]
				mutex.release()
				self.barbero.cortePelo(c)
			else:
				mutex.release()
				print ('Aaah, todo hecho, voy a dormir')
				barbero.sleep()
				print ('Barbero se levanta')
	
	def entraBarberia(self, cliente):
		mutex.acquire()
		print ('>> {0} entra a la tienda y busca una silla'.format(cliente.name))

		if len(self.clientesEspera) == self.numeroSillas:
			print ('Esperando la sala está llena, {0} se va.'.format(cliente.name))
			mutex.release()
		else:
			print ('{0} se ha sentado en la sala de espera'.format(cliente.name))
			self.clientesEspera.append(c)	
			mutex.release()
			barbero.wakeUp()

class Cliente:
	def __init__(self, name):
		self.name = name

class Barbero:
	barberWorkingEvent = Event()

	def sleep(self):
		self.barberWorkingEvent.wait()

	def wakeUp(self):
		self.barberWorkingEvent.set()

	def cortePelo(self, cliente):
		#Set barber as busy 
		self.barberWorkingEvent.clear()

		print ('{0} se está cortando el pelo'.format(cliente.name))

		randomHairCuttingTime = random.randrange(duracionMinCorte, duracionMaxCorte+1)
		time.sleep(randomHairCuttingTime)
		print ('{0} está hecho'.format(cliente.name))


if __name__ == '__main__':
	clientes = []
	clientes.append(Cliente('Josefa'))
	clientes.append(Cliente('Pepe'))
	clientes.append(Cliente('Iris'))
	clientes.append(Cliente('Alex'))
	clientes.append(Cliente('Andrea'))
	clientes.append(Cliente('Alberto'))
	clientes.append(Cliente('Mario'))
	clientes.append(Cliente('Sergio'))
	clientes.append(Cliente('Javier'))
	clientes.append(Cliente('Raúl'))
	clientes.append(Cliente('Benito'))
	clientes.append(Cliente('Pablo'))
	clientes.append(Cliente('Bruno'))
	clientes.append(Cliente('Carlos'))
	clientes.append(Cliente('Tomas'))
	clientes.append(Cliente('Hugo'))
	clientes.append(Cliente('Lorenzo'))

	barbero = Barbero()

	barberia = Barberia(barbero, numeroSillas=1)
	barberia.abrirTienda()

	while len(clientes) > 0:
		c = clientes.pop()	
		#New customer enters the barbershop
		barberia.entraBarberia(c)
		intervaloCliente = random.randrange(intervaloMinCliente,intervaloMaxCliente+1)
		time.sleep(intervaloCliente)
