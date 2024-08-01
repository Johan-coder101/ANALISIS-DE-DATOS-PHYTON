import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import tkinter.messagebox as messagebox

c_negro = '#101010'
c_morado = '#7f5af0'
c_verde = '#2cb67d'
c_amarillo = ''

documento = 'DATA_INGRESANTES_SIN_ACENTOS.csv'
df = pd.read_csv(documento)
total_datos = 6536

def buscar_ingresante(fecha_nacimiento, escuela, provincia_nacimiento): 
    ingresantes = df[(df['F_NACIMIENTO'] == fecha_nacimiento) & 
                    (df['ESCUELA DE PROFESIONAL'] == escuela.upper()) &
                    (df['DISTRITO_NACIMIENTO'] == provincia_nacimiento.upper())]

    if not ingresantes.empty:
        for i, datos_ingresante in ingresantes.iterrows():
            print("Se encontro al estud")
            mostrar_ventana_datos(datos_ingresante)
            mostrar_grafico(datos_ingresante)
    else:
        print("No se encontraron datos para el ingresante con fecha de nacimiento {}, escuela {} y provincia de nacimiento {}.".format(fecha_nacimiento, escuela, provincia_nacimiento))
        mensaje = "No se encontraron datos para el ingresante con: \n Fecha de Nacimiento=> {} \n Escuela Profesional=> {} \n Provincia de Nacimiento=> {}.".format(fecha_nacimiento, escuela, provincia_nacimiento)
        messagebox.showinfo("Alerta", mensaje)

def mostrar_ventana_datos(datos_ingresante):
    ventana_datos = tk.Toplevel()
    ventana_datos.title('Datos del Ingresante')

    def cerrar_ventana():
        ventana_datos.destroy()

    etiquetas_datos = [
        f"Tipo de Examen: {datos_ingresante['MODALIDAD']}",
        f"Escuela: {datos_ingresante['ESCUELA DE PROFESIONAL']}",
        f"Sexo: {datos_ingresante['SEXO']}",
        f"Lugar de Origen: {datos_ingresante['DEPARTAMENTO_NACIMIENTO']}, {datos_ingresante['PROVINCIA_NACIMIENTO']}, {datos_ingresante['DISTRITO_NACIMIENTO']}",
        f"Año de Egreso: {datos_ingresante['AÑO_EGRESO']}",
        f"Tipo de Colegio: {datos_ingresante['TIPO_COLEGIO']}",
        f"Nombre del Colegio: {datos_ingresante['NOMBRE_COLEGIO']}",
        f"Puntaje Total: {datos_ingresante['PUNTAJE_TOTAL']}"
    ]

    for i, etiqueta in enumerate(etiquetas_datos):
        tk.Label(ventana_datos, text=etiqueta, padx=10, pady=5).grid(row=i, column=0, sticky='w')

    tk.Button(ventana_datos, text='Cerrar', command=cerrar_ventana).grid(row=len(etiquetas_datos), column=0, pady=10)

def mostrar_grafico(ingresante):
    media_puntaje_total = df['PUNTAJE_TOTAL'].mean()
    puntaje_ingresante = float(ingresante['PUNTAJE_TOTAL'])

    plt.figure(figsize=(8, 6))
    plt.bar(['Media', 'Ingresante'], [media_puntaje_total, puntaje_ingresante], color=['skyblue', 'orange'])
    plt.title('Comparación de Puntaje Total con la Media')
    plt.ylabel('Puntaje Total')
    plt.show()