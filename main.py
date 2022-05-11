from threading import Thread, Lock, Event
import time, random

mutex = Lock() # mutex for critical section

#Interval in seconds
intervaloMinCliente = 5
intervaloMaxCliente = 15
duracionMinCorte = 3
duracionMaxCorte = 15

#Eventos
class Barberia:
	clientesEspera = []

	def __init__(self, barbero, numeroSillas):
		self.barbero = barbero
		self.numeroSillas = numeroSillas #Número de sillas disponibles
		print ('Barbería se inicializa con {0} silla'.format(numeroSillas)) #Se imprime el número de sillas
		print ('Intervalo mínimo del cliente {0}'.format(intervaloMinCliente)) #Se imprime el intervalo mínimo del cliente
		print ('Intervalo máximo del cliente {0}'.format(intervaloMaxCliente)) #Se imprime el intervalo máximo del cliente
		print ('Duración mínima del corte {0}'.format(duracionMinCorte)) #Se imprime la duración mínima del corte
		print ('Duración máxima del corte {0}'.format(duracionMaxCorte)) #Se imprime la duración máxima del corte
		print ('---------------------------------------') #Se imprime una línea de separación

#Cliente
	def abrirTienda(self):
		print ('Barbería está abriendo')
		workingThread = Thread(target = self.barberoATrabajar) #Crea un hilo para el barbero
		workingThread.start() #Se inicia el hilo

#Barbero
	def barberoATrabajar(self):
		while True:
			mutex.acquire() #Se bloquea el acceso a la sala de espera

			if len(self.clientesEspera) > 0: #Si hay clientes en la sala de espera
				c = self.clientesEspera[0] #Se toma el primer cliente de la sala de espera
				del self.clientesEspera[0] #Se elimina el cliente de la sala de espera
				mutex.release()
				self.barbero.cortePelo(c) #Se le pide al barbero que corte el pelo
			else: #Si no hay clientes en la sala de espera
				mutex.release() #Se libera el acceso a la sala de espera
				print ('Aaah, todo hecho, voy a dormir')
				barbero.sleep() #Se duerme
				print ('Barbero se levanta')

	def entraBarberia(self, cliente): #Método para entrar a la barbería
		mutex.acquire() #Se bloquea el acceso a la sala de espera
		print ('>> {0} entra a la tienda y busca una silla'.format(cliente.name)) #Se imprime el nombre del cliente

		if len(self.clientesEspera) == self.numeroSillas: #Si no hay sillas disponibles
			print ('Esperando la sala está llena, {0} se va.'.format(cliente.name)) #Se imprime el nombre del cliente
			mutex.release() #Se libera el acceso a la sala de espera
		else:
			print ('{0} se ha sentado en la sala de espera'.format(cliente.name)) #Se imprime el nombre del cliente
			self.clientesEspera.append(c) #Se añade el cliente a la sala de espera
			mutex.release() #Se libera el acceso a la sala de espera
			barbero.wakeUp() #Se despierta el barbero

class Cliente: #Clase para los clientes
	def __init__(self, name):
		self.name = name

class Barbero: #Clase para el barbero
	barberWorkingEvent = Event() #Evento para saber si el barbero está trabajando

	def sleep(self): #Método para dormir
		self.barberWorkingEvent.wait() #Espera a que el barbero esté libre

	def wakeUp(self): #Método para despertar
		self.barberWorkingEvent.set() #Se despierta el barbero

	def cortePelo(self, cliente):
		#Set barber as busy
		self.barberWorkingEvent.clear() #Se limpia el evento

		print ('{0} se está cortando el pelo'.format(cliente.name)) #Se imprime el nombre del cliente

		randomHairCuttingTime = random.randrange(duracionMinCorte, duracionMaxCorte+1) #Se genera un tiempo de corte aleatorio
		time.sleep(randomHairCuttingTime) #Se duerme el cliente
		print ('{0} está hecho'.format(cliente.name)) #Se imprime el nombre del cliente


if __name__ == '__main__':
	clientes = [] #Lista de clientes
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

	barbero = Barbero() #Se crea el barbero

	barberia = Barberia(barbero, numeroSillas=1) #Se crea la barbería
	barberia.abrirTienda() #Se abre la tienda

	while len(clientes) > 0: #Mientras haya clientes
		c = clientes.pop() #Se saca un cliente
		#New customer enters the barbershop
		barberia.entraBarberia(c) #Se entra a la barbería
		intervaloCliente = random.randrange(intervaloMinCliente,intervaloMaxCliente+1) #Se genera un intervalo aleatorio
		time.sleep(intervaloCliente) #Se duerme el cliente
