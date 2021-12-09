import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep



port = 'COM5'
board = Arduino(port)


# Pines de los servos
servoPinCodo = 11;
servoPinPinza = 10;
servoPinBase = 9;

# Pines asignados a la funcion de SERVO
board.digital[servoPinPinza].mode = SERVO
board.digital[servoPinCodo].mode = SERVO
board.digital[servoPinBase].mode = SERVO

# Potenciometros
potenciometroSuperior = board.get_pin('a:0:i')
potenciometroMedio = board.get_pin('a:1:i')
potenciometroInferior = board.get_pin('a:2:i')
# Angulo maximo de los servos
maximoAngulo = 170
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