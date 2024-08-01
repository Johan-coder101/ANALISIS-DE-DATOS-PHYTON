import pandas as pd
import tkinter as tk
from tkinter import ttk
import datos as dt  # Suponiendo que 'datos' es el archivo donde tienes definidas tus funciones de visualización
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

documento = 'DATA_INGRESANTES_SIN_ACENTOS.csv'
df = pd.read_csv(documento)
total_datos = 6536

def visualizar_grafico():
    selected_option = graficos_var.get()
    
    # Limpiar el marco de gráfico antes de mostrar un nuevo gráfico
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    
    # Para visualizar el gráfico según la opción seleccionada
    if selected_option == 'Tipo de Examen':
        dt.modalidad_examen()
    elif selected_option == 'Escuelas Profesionales':
        dt.grafico_escuela_general()
    elif selected_option == 'Escuelas Profesionales Top-3':
        dt.grafico_escuela_top3()
    elif selected_option == 'Escuelas Profesionales Menos Ingresantes':
        dt.grafico_escuela_bottom3()
    elif selected_option == 'Fechas de Cumpleaños':
        dt.grafico_fechas_de_nacimiento()
    elif selected_option == 'Pais de Nacimiento':
        dt.pais_de_nacimiento()
    elif selected_option == 'Departamentos':
        dt.visualizar_por_departamento()
    elif selected_option == 'Provincia':
        dt.visualizar_por_provincia()
    elif selected_option == 'Distritos':
        dt.visualizar_top_10_distritos()
    elif selected_option == 'Estado Civil':
        dt.estado_civil()
    elif selected_option == 'Año de Egreso':
        dt.anio_egreso()
    elif selected_option == 'Tipo de Colegio':
        dt.tipo_de_colegio()
    elif selected_option == 'Colegios':
        dt.colegio_del_ingresante()
    elif selected_option == 'Departamento-Colegios':
        dt.departamentos_con_mas_ingresantes()
    elif selected_option == 'Provincia-Colegios':
        dt.provincias_con_mas_ingresantes()
    elif selected_option == 'Distrito-Colegios':
        dt.distritos_con_mas_ingresantes()
    elif selected_option == 'Estado Biometrico':
        dt.estado_biometrico()
    elif selected_option == 'Primeros 33 Puntajes Máximos':
        dt.grafico_puntajes_maximos_primeros()
    elif selected_option == 'Últimos 33 Puntajes Máximos':
        dt.grafico_puntajes_maximos_ultimos()
    elif selected_option == 'Mapa de Calor UNA Puno':
        dt.mapa_calor_una_puno()
    
    # Mostrar el gráfico en el marco
    if plt.gcf().get_axes():  # Verificar si hay gráficos para mostrar
        canvas = FigureCanvasTkAgg(plt.gcf(), master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Crear la ventana principal
root = tk.Tk()
root.title('Visualizador de Gráficos')

# Crear variables
graficos_var = tk.StringVar()
graficos_var.set('Selecciona un gráfico')

# Crear lista de opciones desplegables
opciones_graficos = ['Tipo de Examen', 
                     'Escuelas Profesionales',
                     'Escuelas Profesionales Top-3',
                     'Escuelas Profesionales Menos Ingresantes',
                     'Fechas de Cumpleaños',
                     'Pais de Nacimiento',
                     'Departamentos',
                     'Provincia',
                     'Distritos',
                     'Estado Civil',
                     'Año de Egreso',
                     'Tipo de Colegio',
                     'Colegios',
                     'Departamento-Colegios',
                     'Provincia-Colegios',
                     'Distrito-Colegios',
                     'Estado Biometrico',
                     'Primeros 33 Puntajes Máximos',
                     'Últimos 33 Puntajes Máximos',
                     'Mapa de Calor UNA Puno']  # Agregamos la opción del mapa de calor

dropdown_graficos = ttk.Combobox(root, textvariable=graficos_var, values=opciones_graficos, state='readonly')
dropdown_graficos.grid(row=0, column=0, padx=10, pady=10)

# Crear botón de visualización
btn_visualizar = ttk.Button(root, text='Visualizar', command=visualizar_grafico)
btn_visualizar.grid(row=0, column=1, padx=10, pady=10)

# Crear un marco para los gráficos
frame_grafico = tk.Frame(root)
frame_grafico.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Iniciar el bucle principal
root.mainloop()