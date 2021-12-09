import numpy as np
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep




port = 'COM5'
board = Arduino(port)
#i = 0;
#j = 0;
#iGrabar = 0;
#jGrabar = 0;
#iGrabarActual = 0;
#iReproducir = 0;
#jReproducir = 0;
#valorPOTBase = 0;
#anguloBase = 0;
#valorPOTCodo = 0;
#anguloCodo = 0;
#valorPOTPinza = 0;
#anguloPinza = 0;
#ultimaFila = 0; 
#anguloBaseRep = 0;
#anguloCodoRep = 0;
#anguloPinzaRep = 0;
#angulo1 = 0;
#angulo2 = 0;
#angulo3 = 0;
servoPinCodo = 11
servoPinPinza = 10
servoPinBase = 9
board.digital[servoPinPinza].mode = SERVO
board.digital[servoPinCodo].mode = SERVO
board.digital[servoPinBase].mode = SERVO
POTBase = board.get_pin('a:0:i')
POTCodo = board.get_pin('a:1:i')
POTPinza = board.get_pin('a:2:i')
iterator = pyfirmata.util.Iterator(board)
iterator.start()
def Guardar():
		board.digital[6].write(90)
		print("Guardaste")
while True:

	def Reproducir():
		print("Reproduciste")
	def Borrar():
		print("Borraste")
