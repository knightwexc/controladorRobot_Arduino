import tkinter as tk
from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image, ImageTk

ventana = Tk()
ventana.resizable(False, False)
ventana.title('Actividad en clase')

# Logica ---------------------------------------------------

current_value1 = tk.IntVar()
current_value2 = tk.IntVar()
current_value3 = tk.IntVar()
def get_current_value1():
    return '{: .2f}'.format(current_value1.get())
def get_current_value2():
    return '{: .2f}'.format(current_value2.get())
def get_current_value3():
    return '{: .2f}'.format(current_value3.get())
def slider_changed1(event):
    value1label.configure(text=get_current_value1())
def slider_changed2(event):
    value2label.configure(text=get_current_value2())
def slider_changed3(event):
    value3label.configure(text=get_current_value3())
# Imagen ---------------------------------------------------------------------------------------------------------
img = PhotoImage(file="C:/Users/Jonathan/Pictures/brazo.png")
imagen = img.subsample(9, 4)

# Entradas de angulos ---------------------------------------------------------------------------------------------
e1 = Entry(ventana,width=4)
e2 = Entry(ventana,width=4)
e3 = Entry(ventana,width=4)
e1Label = Label(ventana, text="S1:")
e2Label = Label(ventana, text="S2:")
e3Label = Label(ventana, text="S3:")


#SLIDER 1 -------------------------------------------------------------------------------------------------------
# Definicion de widgets
value1label = ttk.Label(ventana, text=get_current_value1())
slider1Label = ttk.Label(ventana, text='Slider1:',)
#  slider
slider1 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed1, variable=current_value1)
# value label 
value1label = ttk.Label(ventana, text=get_current_value1())
#SLIDER 2 -------------------------------------------------------------------------------------------------------
# Definicion de widgets
value2label = ttk.Label(ventana, text=get_current_value2())
slider2Label = ttk.Label(ventana, text='Slider2:',)
#  slider
slider2 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed2, variable=current_value2)
# value label 
value2label = ttk.Label(ventana, text=get_current_value2())
#SLIDER 3 -------------------------------------------------------------------------------------------------------
# Definicion de widgets
value3label = ttk.Label(ventana, text=get_current_value3())
slider3Label = ttk.Label(ventana, text='Slider3:',)
#  slider
slider3 = ttk.Scale(ventana, from_=10, to=170, orient='horizontal',command=slider_changed3, variable=current_value3)
# value label 
value3label = ttk.Label(ventana, text=get_current_value3())


# Grids - posiciones ---------------------------------------------------------------------------------------------
slider1.grid(       row=0, column=3)
value1label.grid(   row=0, column=4)
slider1Label.grid(  row=0, column=2)

slider2.grid(       row=1, column=3)
value2label.grid(   row=1, column=4)
slider2Label.grid(  row=1, column=2)

slider3.grid(       row=2, column=3)
value3label.grid(   row=2, column=4)
slider3Label.grid(  row=2, column=2)

Label(ventana, image=imagen,).grid(row=0 ,column= 0,columnspan = 1, rowspan = 3, padx = 5, pady = 5)
e1Label.grid(       row=3, column=0)
e1.grid(            row=3, column=1)
e2Label.grid(       row=3, column=2)
e2.grid(            row=3, column=3)
e3Label.grid(       row=3, column=4)
e3.grid(            row=3, column=5)

ventana.mainloop()
