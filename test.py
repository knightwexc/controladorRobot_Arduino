import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep




class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

       board = Arduino('COM3')
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
           aCodo= int(board.digital[servoPinCodo].read())
           aPinza= int(board.digital[servoPinPinza].read())
           aBase = int(board.digital[servoPinBase].read())
           posiciones = np.array([aCodo,aPinza,aBase])
        #    guardado = ([posiciones])
           global guardado
           guardado = []
           guardado.append(posiciones)
           
           guardado = np.asarray(guardado)
           print(guardado)
           
           
       def Reproducir():
           for i in guardado:
               print(i)
               
       def Borrar():
           print("Configurando")
           board.digital[servoPinBase].write(20)
           sleep(0.5)

       self.grid_rowconfigure(0, weight=1)
       self.grid_rowconfigure(5, weight=1)
       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(6, weight=1)

       current_value1 = tk.IntVar()
       current_value2 = tk.IntVar()
       current_value3 = tk.IntVar()

       

       global canvas
       canvas = Canvas(self,width=200,height=200)
       

       canvas.create_line(0,200, 200,200)
       a1= (100,200)
       a2= (100,80)
       canvas.create_line(a1, a2)
       b2=(120,20)
       canvas.create_line(a2, b2)
       c2=(100,0)
       canvas.create_line(b2, c2)

       sliderFrame = Frame(self)
       entryFrame = Frame(self)
       buttonFrame = Frame(self)

       def get_current_value1():
            pinza = '{:d}'.format(current_value1.get())
            board.digital[servoPinPinza].write(pinza)
            return pinza
       def get_current_value2():
            codo = '{:d}'.format(current_value2.get())
            board.digital[servoPinCodo].write(codo)
            return codo
       def get_current_value3():
            base = '{:d}'.format(current_value3.get())
            board.digital[servoPinBase].write(base)
            return base
       def slider_changed1(event):
           value1label.configure(text=get_current_value1())
           e1.delete(0,END)
           e1.insert(0,get_current_value1())
       def slider_changed2(event):
           value2label.configure(text=get_current_value2())
           e2.delete(0,END)
           e2.insert(0,get_current_value2())
       def slider_changed3(event):
            value3label.configure(text=get_current_value3())
            e3.delete(0,END)
            e3.insert(0,get_current_value3())

       e1 = tk.Entry(entryFrame, width=4)
       e2 = tk.Entry(entryFrame, width=4)
       e3 = Entry(entryFrame, width=4)
       e1Label = Label(entryFrame, text="S1:")
       e2Label = Label(entryFrame, text="S2:")
       e3Label = Label(entryFrame, text="S3:")


       value1label = ttk.Label(sliderFrame, text=get_current_value1())
       slider1Label = ttk.Label(sliderFrame, text='Slider1:',)
       slider1 = ttk.Scale(sliderFrame, from_=10, to=170, orient='horizontal',command=slider_changed1, variable=current_value1)
       value1label = ttk.Label(sliderFrame, text=get_current_value1())
       value2label = ttk.Label(sliderFrame, text=get_current_value2())
       slider2Label = ttk.Label(sliderFrame, text='Slider2:',)
       slider2 = ttk.Scale(sliderFrame, from_=10, to=170, orient='horizontal',command=slider_changed2, variable=current_value2)
       value2label = ttk.Label(sliderFrame, text=get_current_value2())
       value3label = ttk.Label(sliderFrame, text=get_current_value3())
       slider3Label = ttk.Label(sliderFrame, text='Slider3:',)
       slider3 = ttk.Scale(sliderFrame, from_=10, to=170, orient='horizontal',command=slider_changed3, variable=current_value3)
       value3label = ttk.Label(sliderFrame, text=get_current_value3())

       Guardar = ttk.Button(buttonFrame,command=Guardar, text="Guardar")
       Reproducir = ttk.Button(buttonFrame,command=Reproducir, text="Reproducir")
       Borrar = ttk.Button(buttonFrame,command=Borrar, text="Borrar")


       canvas.grid(         row=1 ,column= 1,rowspan=2)
       sliderFrame.grid(    row=1,column=2,sticky= N)
       entryFrame.grid(     row=2,column=2,sticky= N)
       buttonFrame.grid(    row=3,column=2,sticky= N)

       slider1Label.grid(  row=0, column=0)
       slider1.grid(       row=0, column=1)
       value1label.grid(   row=0, column=2)
       
       slider2Label.grid(  row=1, column=0)
       slider2.grid(       row=1, column=1)
       value2label.grid(   row=1, column=2)
       
       slider3Label.grid(  row=2, column=0)
       slider3.grid(       row=2, column=1)
       value3label.grid(   row=2, column=2)
       Guardar.grid(       row=0, column=0)
       Reproducir.grid(    row=1, column=0)
       Borrar.grid(        row=2, column=0)


       e1Label.grid(       row=0, column=1)
       e1.grid(            row=0, column=2)
       e2Label.grid(       row=0, column=3)
       e2.grid(            row=0, column=4)
       e3Label.grid(       row=0, column=5)
       e3.grid(            row=0, column=6)




























class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       global canvas
       canvas.grid(         row=1 ,column= 1,rowspan=2)




















class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Manual", command=p1.show)
        b2 = tk.Button(buttonframe, text="Cálculo", command=p2.show)
        b3 = tk.Button(buttonframe, text="Simulación", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()

