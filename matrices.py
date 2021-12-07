import numpy as np
import pandas as pd
from math import cos, sin


def exportar(matrizAi, matrizA1, matrizA2, matrizA3, matrizT):
    columnas = np.array(['θ', 'd', 'a', 'α'])
    fila = np.arange(1, 4)

    dfAi = pd.DataFrame(
        matrizAi, index=fila, columns=columnas)
    dfA1 = pd.DataFrame(
        matrizA1, index=fila, columns=columnas)
    dfA2 = pd.DataFrame(
        matrizA2, index=fila, columns=columnas)
    dfA3 = pd.DataFrame(
        matrizA3, index=fila, columns=columnas)
    dfT = pd.DataFrame(
        matrizT, index=fila, columns=columnas)

    with pd.ExcelWriter("MatrizCinetica.xlsx") as writer:
        dfAi.to_excel(writer, sheet_name="MatrizAi",
                      index_label="Articulación", merge_cells=False)
        dfA1.to_excel(writer, sheet_name="MatrizA1",
                      index_label="Articulación", merge_cells=False)
        dfA2.to_excel(writer, sheet_name="MatrizA2",
                      index_label="Articulación", merge_cells=False)
        dfA3.to_excel(writer, sheet_name="MatrizA3",
                      index_label="Articulación", merge_cells=False)
        dfT.to_excel(writer, sheet_name="MatrizT",
                     index_label="Articulación", merge_cells=False)

        return dfAi, dfA1, dfA2, dfA3, dfT


def matrices(anguloSuperior, anguloMedio, anguloInferior):
    '''Articulacion 1'''
    teta1 = anguloSuperior  # Giro en z
    d1 = 10  # Distancia de z
    a1 = 0  # Distancia de x
    alfa1 = 0  # Giro en x

    '''Articulacion 2'''
    teta2 = anguloMedio  # Giro en z
    d2 = 2  # Distancia de z
    a2 = 0  # Distancia de x
    alfa2 = 0  # Giro en x

    '''Articulacion 3'''
    teta3 = anguloInferior  # Giro en z
    d3 = 7.5  # Distancia de z
    a3 = 0  # Distancia de x
    alfa3 = 0  # Giro en x

    print()
    matrizAi = np.array([[teta1, d1, a1, alfa1],
                        [teta2, d2, a2, alfa2],
                        [teta3, d3, a3, alfa3]])

    print(matrizAi)

    print('---------------------------------------------------------------------------------------------------')
    print('Matriz A1')

    matrizA1 = np.array([[cos(teta1), -cos(alfa1) * sin(teta1), sin(alfa1) * sin(teta1), a1 * cos(teta1)],
                        [sin(teta1), cos(alfa1) * cos(teta1), -
                        sin(alfa1) * cos(teta1), a1 * sin(teta1)],
                        [0, 0, 0, 1]])

    print(matrizA1)

    print()
    print('Matriz A2')

    matrizA2 = np.array([[cos(teta2), -cos(alfa2) * sin(teta2), sin(alfa2) * sin(teta2), a2 * cos(teta2)],
                        [sin(teta2), cos(alfa2) * cos(teta2), -
                        sin(alfa2) * cos(teta2), a2 * sin(teta2)],
                        [0, 0, 0, 1]])

    print(matrizA2)

    print()
    print('Matriz A3')

    matrizA3 = np.array([[cos(teta3), -cos(alfa3) * sin(teta3), sin(alfa3) * sin(teta3), a3 * cos(teta3)],
                        [sin(teta3), cos(alfa3) * cos(teta3), -
                        sin(alfa3) * cos(teta3), a3 * sin(teta3)],
                        [0, 0, 0, 1]])

    print(matrizA3)

    print('---------------------------------------------------------------------------------------------------')
    print('Matriz T')

    matrizT = matrizA1 * matrizA2 * matrizA3
    print(matrizT)

    exportar(matrizAi, matrizA1, matrizA2, matrizA3, matrizT)