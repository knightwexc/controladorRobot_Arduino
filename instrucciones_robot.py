from pyfirmata import Arduino, SERVO
from time import sleep
import pyfirmata


port = 'COM3'
board = Arduino(port)
# Pines de los servos
servoSuperior = 10
servoMedio = 9
servoInferior = 8

# Pines asignados a la funcion de SERVO
board.digital[servoSuperior].mode = SERVO
board.digital[servoMedio].mode = SERVO
board.digital[servoInferior].mode = SERVO
# Potenciometros
potenciometroSuperior = board.get_pin('a:0:i')
potenciometroMedio = board.get_pin('a:1:i')
potenciometroInferior = board.get_pin('a:2:i')
# Angulo maximo de los servos
maximoAngulo = 180
# Iniciar los potenciometros
it = pyfirmata.util.Iterator(board)
it.start()

# Funciones de giro


def rotateServoSuperior(pin, angulo):
    board.digital[pin].write(angulo)
    sleep(0.015)


def rotateServoMedio(pin, angulo):
    board.digital[pin].write(angulo)
    sleep(0.015)


def rotateServoInferior(pin, angulo):
    board.digital[pin].write(angulo)
    sleep(0.015)


while True:
   
    # -------------------------------------------------------------------
    analog_value1 = potenciometroSuperior.read()
    sleep(0.5)

    if analog_value1 == None:
        print('no pasa nada')
    else:
        anguloSuperior = analog_value1 * maximoAngulo
        print(anguloSuperior)

        rotateServoSuperior(servoSuperior, anguloSuperior)
# -------------------------------------------------------------------
    analog_value2 = potenciometroMedio.read()
    sleep(0.5)

    if analog_value2 == None:
        print('no pasa nada')
    else:
        anguloMedio = analog_value2 * maximoAngulo
        print(anguloMedio)

        rotateServoMedio(servoMedio, anguloMedio)
# -------------------------------------------------------------------
    analog_value3 = potenciometroInferior.read()
    sleep(0.5)

    if analog_value3 == None:
        print('no pasa nada')
    else:
        anguloInferior = analog_value3 * maximoAngulo
        print(anguloInferior)

        rotateServoSuperior(servoInferior, anguloInferior)