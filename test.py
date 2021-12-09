import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from numpy import dtype, savetxt
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep
import csv
import pandas as pd
import math
from math import cos,sin
from matrices import *
from pandastable import Table, TableModel




class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

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
           aCodo= int(board.digital[servoPinCodo].read())
           aPinza= int(board.digital[servoPinPinza].read())
           aBase = int(board.digital[servoPinBase].read())
           posiciones = np.array([[aCodo],[aPinza],[aBase]])
           

           guardado = []
           guardado.append(posiciones)
           guardado = np.asarray(guardado)
           guardado = guardado.tolist()
           with open("data.csv", 'a', newline='') as csvfile:
              writer = csv.writer(csvfile, delimiter=',')
              writer.writerows(guardado)

        #   with open('data.csv', 'a') as abc:
        #       np.savetxt(abc, guardado, fmt='%i', delimiter=',',comments='')
           
       def Reproducir():
           df = pd.read_csv('data.csv', header=None)
           valores = df.to_numpy()
           print(valores)
           for i in valores:
               pinza = int(i[0].lstrip("[").rstrip("]"))
               codo = int(i[1].lstrip("[").rstrip("]"))
               base = int(i[2].lstrip("[").rstrip("]"))
               board.digital[servoPinPinza].write(pinza)
               board.digital[servoPinCodo].write(codo)
               print(base)
               board.digital[servoPinBase].write(base)
               sleep(2)
           

               
       def Borrar():
           f = open("data.csv", "w")
           f.truncate()
           f.close()

       self.grid_rowconfigure(0, weight=1)
       self.grid_rowconfigure(5, weight=1)
       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(6, weight=1)

       current_value1 = tk.IntVar()
       current_value2 = tk.IntVar()
       current_value3 = tk.IntVar()

       

       global canvas
       canvas = Canvas(self,width=200,height=200)
       

       canvas.create_polygon(0,200, 200,200,width=3,outline="black")
       canvas.create_polygon(100,200, 100,80,width=3,outline="black")
       brazo = canvas.create_polygon(100,80,193,45,width=3,outline="black")
       pinza = canvas.create_polygon(120,20, 100,0,width=3,outline="black")



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
            angle_in_degress = int(codo) - 20
            angle_in_radians = float(angle_in_degress) * math.pi / 180
            line_length = 100
            center_x = 100
            center_y = 80
            end_x = center_x + line_length * math.cos(angle_in_radians)
            end_y = center_y + line_length * math.sin(angle_in_radians)
            print(end_x)
            print(end_y)
            #line = canvas.create_polygon(center_x,center_y,end_x,end_y,width=3, outline="white")
            
            canvas.coords(brazo, center_x,center_y,end_x,end_y)
            canvas.coords(pinza, center_x,center_y,end_x,end_y)



            #image = Image.open('C:/Users/Jonathan/Pictures/884.png')
            #res = image.resize((3, 100))
            #res.place(x=100, y=80)
            #res.rotate(angle_in_degress)
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

       tablaFrame = Frame(self)
       botonesFrame = Frame(self)
       def calcular():
          df = pd.read_csv('data.csv', header=None)
          ultimoValor = df.iloc[-1:]
          modificar = ultimoValor.to_numpy(dtype="str")
          for i in modificar:
             pinza = int(i[0].lstrip("[").rstrip("]"))
             codo = int(i[1].lstrip("[").rstrip("]"))
             base = int(i[2].lstrip("[").rstrip("]"))
             matrices(pinza,codo,base)


       def matrices(anguloSuperior, anguloMedio, anguloInferior):
           teta1 = anguloInferior  # Giro en z
           d1 = 16.3  # Distancia de z
           a1 = 0  # Distancia de x
           alfa1 = 0  # Giro en x

           teta2 = anguloMedio  # Giro en z
           d2 = 9.6  # Distancia de z
           a2 = 0  # Distancia de x
           alfa2 = 0  # Giro en x

           teta3 = anguloSuperior  # Giro en z
           d3 = 0.5  # Distancia de z
           a3 = 0  # Distancia de x
           alfa3 = 0  # Giro en x

           matrizAi = np.array([[teta1, d1, a1, alfa1], [teta2, d2, a2, alfa2], [teta3, d3, a3, alfa3]])

           matrizA1 = np.array([[cos(teta1), -cos(alfa1) * sin(teta1), sin(alfa1) * sin(teta1), a1 * cos(teta1)], [sin(teta1), cos(alfa1) * cos(teta1), - sin(alfa1) * cos(teta1), a1 * sin(teta1)], [0, 0, 0, 1]])

           matrizA2 = np.array([[cos(teta2), -cos(alfa2) * sin(teta2), sin(alfa2) * sin(teta2), a2 * cos(teta2)], [sin(teta2), cos(alfa2) * cos(teta2), -sin(alfa2) * cos(teta2), a2 * sin(teta2)], [0, 0, 0, 1]])

           matrizA3 = np.array([[cos(teta3), -cos(alfa3) * sin(teta3), sin(alfa3) * sin(teta3), a3 * cos(teta3)], [sin(teta3), cos(alfa3) * cos(teta3), - sin(alfa3) * cos(teta3), a3 * sin(teta3)], [0, 0, 0, 1]])

           matrizT = matrizA1 * matrizA2 * matrizA3



           columnas = np.array(['θ', 'd', 'a', 'α'])
           dfAi = pd.DataFrame(matrizAi)
           dfA1 = pd.DataFrame(matrizA1)
           dfA2 = pd.DataFrame(matrizA2)
           dfA3 = pd.DataFrame(matrizA3)
           dfT = pd.DataFrame(matrizT)
           guardado = [[[dfAi],[dfA1],[dfA2],[dfA3],[dfT]]]
           guardado = np.asarray(guardado)
           guardado = guardado.tolist()
           with open("matrices.csv", 'a', newline='') as csvfile:
              writer = csv.writer(csvfile, delimiter=',')
              writer.writerows(guardado)


           df = pd.read_csv('matrices.csv', names=["dfAi", "dfA1", "dfA2", "dfA3","dfT"])
           ultimoValor = df.iloc[-1:]
           dfAi_show = ultimoValor["dfAi"].to_frame()
           self.table = pt = Table(tablaFrame, dataframe=dfAi_show,showtoolbar=True, showstatusbar=True,editable=False)
           pt.grid(         row=1 ,column= 1)
           pt.show()

       def Borrar():
            f = open("matrices.csv", "w")
            f.truncate()
            f.close()


       tablaFrame.grid(         row=1 ,column= 1)
       botonesFrame.grid(         row=1 ,column= 2)
       Calcular = ttk.Button(botonesFrame,command=calcular, text="Calcular")
       Borrar = ttk.Button(botonesFrame,command=Borrar, text="Borrar")
       Calcular.grid(         row=1)
       Borrar.grid(         row=2)




















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

