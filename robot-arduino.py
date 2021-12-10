import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import numpy as np
from numpy import dtype, savetxt
import pyfirmata
from pyfirmata import Arduino, SERVO
from time import sleep
import csv
import pandas as pd
import math
from math import cos,sin
from pandastable import Table, TableModel



board = Arduino('COM5')
servoPinCodo = 11
servoPinPinza = 10
servoPinBase = 9
class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)


       board.digital[servoPinPinza].mode = SERVO
       board.digital[servoPinCodo].mode = SERVO
       board.digital[servoPinBase].mode = SERVO

       board.digital[servoPinPinza].write(10)
       board.digital[servoPinCodo].write(10)
       board.digital[servoPinBase].write(10)
       iterator = pyfirmata.util.Iterator(board)
       iterator.start()
    
       def Guardar():
           aPinza= int(board.digital[servoPinPinza].read())
           aCodo= int(board.digital[servoPinCodo].read())
           aBase = int(board.digital[servoPinBase].read())

           posiciones = np.array([[aPinza],[aCodo],[aBase]])
           if aCodo == 0 and aPinza == 0 and aBase == 0:
               messagebox.showinfo(message="Modifique posiciones antes de guardar posiciones en 0", title="Advertencia")
           else:
               import os
               if os.stat("data.csv").st_size == 0:
                   guardado = []
                   guardado.append(posiciones)
                   guardado = np.asarray(guardado)
                   guardado = guardado.tolist()
                   with open("data.csv", 'a', newline='') as csvfile:
                      writer = csv.writer(csvfile, delimiter=',')
                      writer.writerows(guardado)
               else:
                   df = pd.read_csv('data.csv', header=None)
                   guardado = []
                   guardado.append(posiciones)
                   guardado = np.asarray(guardado)
                   if str(guardado[0,0]) == str(df.iloc[-1,0]) and str(guardado[0,1]) == str(df.iloc[-1,1]) and str(guardado[0,2]) == str(df.iloc[-1,2]):
                      messagebox.showinfo(message="Modifica valores, la posición ya se encuentra registrada", title="Advertencia")
                   else:
                       guardado = guardado.tolist()
                       with open("data.csv", 'a', newline='') as csvfile:
                          writer = csv.writer(csvfile, delimiter=',')
                          writer.writerows(guardado)
           
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
            modPinza = str(pinza)+"°"
            board.digital[servoPinPinza].write(pinza)
            return modPinza
       def get_current_value2():
            codo = '{:d}'.format(current_value2.get())
            modCodo = str(codo)+"°"
            board.digital[servoPinCodo].write(codo)
            angle_in_degress = int(codo) - 180
            angle_in_radians = float(angle_in_degress) * math.pi / 180
            line_length = 100
            center_x = 100
            center_y = 80
            end_x = center_x + line_length * math.cos(angle_in_radians)
            end_y = center_y + line_length * math.sin(angle_in_radians)

            
            canvas.coords(brazo, center_x,center_y,end_x,end_y)
            canvas.coords(pinza, center_x,center_y,end_x,end_y)



            #image = Image.open('C:/Users/Jonathan/Pictures/884.png')
            #res = image.resize((3, 100))
            #res.place(x=100, y=80)
            #res.rotate(angle_in_degress)
            return modCodo
       def get_current_value3():
            base = '{:d}'.format(current_value3.get())
            modBase = str(base)+"°"
            board.digital[servoPinBase].write(base)
            return modBase
       def slider_changed1(event):
           value1label.configure(text=get_current_value1())
           e1.config(state = NORMAL)
           e1.delete(0,END)
           e1.insert(0,get_current_value1())
           e1.config(state = "readonly")
       def slider_changed2(event):
           value2label.configure(text=get_current_value2())
           e2.config(state = NORMAL)
           e2.delete(0,END)
           e2.insert(0,get_current_value2())
           e2.config(state = "readonly")
       def slider_changed3(event):
            value3label.configure(text=get_current_value3())
            e3.config(state = NORMAL)
            e3.delete(0,END)
            e3.insert(0,get_current_value3())
            e3.config(state = "readonly")

       e1 = tk.Entry(entryFrame, width=4,state = "readonly")
       e2 = tk.Entry(entryFrame, width=4,state = "readonly")
       e3 = Entry(entryFrame, width=4,state = "readonly")

       e1.insert(0, '0')
       e2.insert(0, '0')
       e3.insert(0, '0')
       e1Label = Label(entryFrame, text="S1:")
       e2Label = Label(entryFrame, text="S2:")
       e3Label = Label(entryFrame, text="S3:")


       value1label = ttk.Label(sliderFrame, text=get_current_value1())
       slider1Label = ttk.Label(sliderFrame, text='Pinza:',)
       slider1 = ttk.Scale(sliderFrame, from_=10, to=170, orient='horizontal',command=slider_changed1, variable=current_value1)
       value1label = ttk.Label(sliderFrame, text=get_current_value1())
       value2label = ttk.Label(sliderFrame, text=get_current_value2())
       slider2Label = ttk.Label(sliderFrame, text='Codo:',)
       slider2 = ttk.Scale(sliderFrame, from_=10, to=170, orient='horizontal',command=slider_changed2, variable=current_value2)
       value2label = ttk.Label(sliderFrame, text=get_current_value2())
       value3label = ttk.Label(sliderFrame, text=get_current_value3())
       slider3Label = ttk.Label(sliderFrame, text='Base:',)
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
          
          import os
          if os.stat("data.csv").st_size == 0:
             messagebox.showinfo(message="Primero debe guardar una posición del robot", title="Advertencia")
          else:
             df = pd.read_csv('data.csv', header=None)
             ultimoValor = df.iloc[-1:]
             modificar = ultimoValor.to_numpy(dtype="str")
             for i in modificar:
                pinza = int(i[0].lstrip("[").rstrip("]"))
                codo = int(i[1].lstrip("[").rstrip("]"))
                base = int(i[2].lstrip("[").rstrip("]"))
                matrices(pinza,codo,base)


       def matrices(anguloSuperior, anguloMedio, anguloInferior):
           teta1 = anguloInferior  
           d1 = 16.3 
           a1 = 0
           alfa1 = 0

           teta2 = anguloMedio  
           d2 = 9.6 
           a2 = 0
           alfa2 = 0

           teta3 = anguloSuperior  
           d3 = 0.5
           a3 = 0
           alfa3 = 0

           matrizAi = np.array([[teta1, d1, a1, alfa1], [teta2, d2, a2, alfa2], [teta3, d3, a3, alfa3]])

           matrizA1 = np.array([[cos(teta1), -cos(alfa1) * sin(teta1), sin(alfa1) * sin(teta1), a1 * cos(teta1)], [sin(teta1), cos(alfa1) * cos(teta1), - sin(alfa1) * cos(teta1), a1 * sin(teta1)], [0, 0, 0, 1]])

           matrizA2 = np.array([[cos(teta2), -cos(alfa2) * sin(teta2), sin(alfa2) * sin(teta2), a2 * cos(teta2)], [sin(teta2), cos(alfa2) * cos(teta2), -sin(alfa2) * cos(teta2), a2 * sin(teta2)], [0, 0, 0, 1]])

           matrizA3 = np.array([[cos(teta3), -cos(alfa3) * sin(teta3), sin(alfa3) * sin(teta3), a3 * cos(teta3)], [sin(teta3), cos(alfa3) * cos(teta3), - sin(alfa3) * cos(teta3), a3 * sin(teta3)], [0, 0, 0, 1]])

           matrizT = matrizA1 * matrizA2 * matrizA3

           dfAi = pd.DataFrame(matrizAi)
           dfA1 = pd.DataFrame(matrizA1)
           dfA2 = pd.DataFrame(matrizA2)
           dfA3 = pd.DataFrame(matrizA3)
           dfT = pd.DataFrame(matrizT)
           posiciones = np.array([dfAi,dfA1,dfA2,dfA3,dfT])
           guardado = []
           guardado.append(posiciones)
           guardado = np.asarray(guardado)
           guardado = guardado.tolist()
           with open("matrices.csv", 'a', newline='') as csvfile:
              writer = csv.writer(csvfile, delimiter=',')
              writer.writerows(guardado)


           df = pd.read_csv('matrices.csv', names=["dfAi", "dfA1", "dfA2", "dfA3","dfT"])
           ultimoValor = df.iloc[-1:].transpose()
           ultimoValor.insert(0, "Matrices", ["dfAi", "dfA1", "dfA2", "dfA3","dfT"], True)
        #   df = pd.read_csv('matrices.csv', names=["dfAi", "dfA1", "dfA2", "dfA3","dfT"])
        #   ultimoValor = df.iloc[-1:]
        #   dfAi_show = ultimoValor["dfAi"].to_frame()
           self.table = pt = Table(tablaFrame, dataframe=ultimoValor,showtoolbar=True, showstatusbar=True,editable=False, width=450, height=310)
           pt.grid(         row=1 ,column= 1)
           pt.show()

       def Borrar():
            f = open("matrices.csv", "w")
            f.truncate()
            f.close()


       tablaFrame.grid(         row=1 ,column= 1)
       botonesFrame.grid(         row=2 ,column= 1)
       Calcular = ttk.Button(botonesFrame,command=calcular, text="Calcular")
       Borrar = ttk.Button(botonesFrame,command=Borrar, text="Borrar")
       Calcular.grid(         row=0, column= 0)
       Borrar.grid(         row=0, column= 1)




















class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global board
       board.digital[servoPinPinza].write(10)
       board.digital[servoPinCodo].write(10)
       board.digital[servoPinBase].write(10)
       iterator = pyfirmata.util.Iterator(board)
       iterator.start()

       self.grid_rowconfigure(0, weight=1)
       self.grid_rowconfigure(5, weight=1)
       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(6, weight=1)
       
       canvas = Canvas(self,width=200,height=200)
       canvas.create_polygon(0,200, 200,200,width=3,outline="black")
       canvas.create_polygon(100,200, 100,80,width=3,outline="black")
       movimiento_brazo = canvas.create_polygon(100,80,193,45,width=3,outline="black")

       movimientos = [20,120,20,120,50,20,150,160,170]


       def iniciar():
           
           for i in movimientos:
               posicion = i
               print(posicion)
               angle_in_degress = int(posicion) - 170
               angle_in_radians = float(angle_in_degress) * math.pi / 180
               line_length = 100
               center_x = 100
               center_y = 80
               end_x = center_x + line_length * math.cos(angle_in_radians)
               end_y = center_y + line_length * math.sin(angle_in_radians)
               canvas.coords(movimiento_brazo, center_x,center_y,int(end_x),int(end_y))
               canvas.update_idletasks()
               board.digital[servoPinCodo].write(posicion)
               sleep(1)
                


     
       calcular = ttk.Button(self,command=iniciar, text="simular")

       canvas.grid(         row=1 ,column= 1,rowspan=2)
       calcular.grid(         row=5 ,column= 1)









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
    root.wm_geometry("550x550")
    root.mainloop()

