import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep

board = Arduino('COM5')
servoPinCodo = 11
servoPinPinza = 10
servoPinBase = 9
board.digital[servoPinPinza].mode = SERVO
board.digital[servoPinCodo].mode = SERVO
board.digital[servoPinBase].mode = SERVO

board.digital[servoPinPinza].write(0)
board.digital[servoPinCodo].write(0)
board.digital[servoPinBase].write(0)

iterator = pyfirmata.util.Iterator(board)
iterator.start()

def Guardar():
	print(board.digital[9].read())
	sleep(0.5)
def Reproducir():
	print("Reproduciendo")
	sleep(0.5)
def Borrar():
	print("Configurando a 20")
	board.digital[servoPinBase].write(80)
	sleep(0.5)

Guardar()
Reproducir()
Borrar()