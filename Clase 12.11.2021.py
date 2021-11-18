import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


ventana = Tk()
ventana.geometry('500x400')
ventana.resizable(False, False)
ventana.title('Actividad en clase')

# Logica ---------------------------------------------------

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)
ventana.columnconfigure(3, weight=1)
ventana.columnconfigure(4, weight=1)
current_value1 = tk.DoubleVar()
current_value2 = tk.DoubleVar()
current_value3 = tk.DoubleVar()


def get_current_value1():
    return '{: .2f}'.format(current_value1.get())
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def get_current_value3():
    return '{: .2f}'.format(current_value3.get())

def slider_changed1(event1):
    value1label.configure(text=get_current_value1())
def slider_changed2(event2):
    value1label.configure(text=get_current_value2())
def slider_changed3(event3):
    value1label.configure(text=get_current_value3())
#SLIDER 1 -------------------------------------------------------------------------------------------------------
# Definicion de widgets -----------------------
value1label = ttk.Label(ventana, text=get_current_value1())
slider1Label = ttk.Label(ventana, text='Slider1:',)
#  slider
slider1 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed1, variable=current_value1)
# value label ************
value1label = ttk.Label(ventana, text=get_current_value1())
# Grids - posiciones ----------------
slider1.grid(column=3, row=0)
value1label.grid(column=4,row=0)
slider1Label.grid(column=2, row=0)
#-----------------------------------------------------------------------------------------------------------------
#SLIDER 2 -------------------------------------------------------------------------------------------------------
# Definicion de widgets -----------------------
value2label = ttk.Label(ventana, text=get_current_value2())
slider2Label = ttk.Label(ventana, text='Slider2:',)
#  slider
slider2 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed2, variable=current_value2)
# value label ************
value2label = ttk.Label(ventana, text=get_current_value2())
# Grids - posiciones ----------------
slider2.grid(column=3, row=1)
value2label.grid(column=4,row=1)
slider2Label.grid(column=2, row=1)
#-----------------------------------------------------------------------------------------------------------------
#SLIDER 3 -------------------------------------------------------------------------------------------------------
# Definicion de widgets -----------------------
value3label = ttk.Label(ventana, text=get_current_value3())
slider3Label = ttk.Label(ventana, text='Slider3:',)
#  slider
slider3 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed3, variable=current_value3)
# value label ************
value3label = ttk.Label(ventana, text=get_current_value3())
# Grids - posiciones ----------------
slider3.grid(column=3, row=2)
value3label.grid(column=4,row=2)
slider3Label.grid(column=2, row=2)
#-----------------------------------------------------------------------------------------------------------------

photo = PhotoImage(file="C:/Users/knigh/Pictures/brazo.png")
photoimage = photo.subsample(9, 4)
Button(ventana, image=photoimage,).place(x=10, y=10, width=100, height=150)

boton_test1 = ttk.Button(text='salir', command=quit)
boton_test1.place(x=20, y=350, width=100)


ventana.mainloop()
