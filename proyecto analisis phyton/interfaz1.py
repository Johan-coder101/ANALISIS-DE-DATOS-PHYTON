import pandas as pd
import tkinter as tk
from tkinter import ttk, PhotoImage
from customtkinter import CTkFrame, CTkEntry, CTkLabel, CTkButton
import buscar_ingresantes as bi
import datos as dt  
import matplotlib.pyplot as plt
import seaborn as sns

class Interfaz:

    def __init__(self):
        self.file_path = 'DATA_INGRESANTES_SIN_ACENTOS.csv'
        self.df = pd.read_csv(self.file_path)
        self.total_datos = 6536

        self.c_negro = '#101010'
        self.c_morado = '#7f5af0'
        self.c_verde = '#2cb67d'

        self.datos = pd.DataFrame(columns=['Fecha_Nacimiento', 'Escuela', 'Lugar_Nacimiento'])
        self.datos_ingresados = False

        self.root = tk.Tk()
        self.root.geometry('900x700+350+20')
        self.root.minsize(900, 700)
        self.root.config(bg=self.c_negro)
        self.root.title('Datos sobre ingresantes a la UNA Puno el año 2022')

        self.logo = PhotoImage(file='logo.png')
        self.logo = self.logo.subsample(1, 1)

        self.frame = CTkFrame(self.root, fg_color=self.c_negro)
        self.frame.grid(column=0, row=0, sticky='nsew', padx=50, pady=50)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        CTkLabel(self.root, image=self.logo).grid(columnspan=2, row=0)

        self.titul = CTkLabel(self.root, text='BUSCAR DATOS DE INGRESANTES A LA UNA-PUNO 2022',
                              fg_color=self.c_negro, width=220, height=40)
        self.titul.grid(columnspan=2, row=1, padx=4, pady=4)

        self.fecha_nac = CTkEntry(self.root, placeholder_text='Fecha de nacimiento AAAAMMDD',
                                  border_color=self.c_verde, fg_color=self.c_negro, width=220, height=40)
        self.fecha_nac.grid(columnspan=2, row=2, padx=4, pady=4)

        self.escuela = CTkEntry(self.root, placeholder_text='Nombre de la escuela',
                                border_color=self.c_verde, fg_color=self.c_negro, width=220, height=40)
        self.escuela.grid(columnspan=2, row=3, padx=4, pady=4)

        self.distrito = CTkEntry(self.root, placeholder_text='Lugar de nacimiento (distrito)',
                                 border_color=self.c_verde, fg_color=self.c_negro, width=220, height=40)
        self.distrito.grid(columnspan=2, row=4, padx=4, pady=4)

        self.bt_iniciar = CTkButton(self.root, border_color=self.c_verde, fg_color=self.c_negro,
                                    hover_color=self.c_verde, corner_radius=12, border_width=2,
                                    text='Buscar Estudiante', command=self.guardar_datos)
        self.bt_iniciar.grid(columnspan=2, row=5, padx=4, pady=4)

        self.opciones_graficos = ['GRAFICOS',
                                  'Tipo de Examen', 
                                  'Escuelas Profesionales',
                                  'Escuelas Profesionales Top-3',
                                  'Escuelas Profesionales Menos Ingresantes',
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
                                  'Matriz de correlacion']
        self.graficos_var = tk.StringVar()
        self.graficos_var.set(self.opciones_graficos[0])

        self.dropdown_graficos = ttk.Combobox(self.root, textvariable=self.graficos_var, values=self.opciones_graficos, state='readonly')
        self.dropdown_graficos.grid(row=6, column=0, padx=10, pady=10)
        
        style = ttk.Style(self.root)
        style.configure('Custom.TButton', foreground=self.c_negro, background=self.c_verde, width=15, height=2, font=('Arial', 10))

        self.btn_visualizar = ttk.Button(self.root, text='Visualizar', command=self.visualizar_grafico, style='Custom.TButton')
        self.btn_visualizar.grid(row=6, column=1, padx=80, pady=10)

        style.configure('Custom.TButton', foreground=self.c_negro, background=self.c_verde, width=15, height=2, font=('Arial', 10))

        self.root.call('wm', 'iconphoto', self.root._w, self.logo)

        self.root.mainloop()

    def obtener_cantidad_elementos(self):
        return len(self.datos)

    def guardar_datos(self):
        fecha_nacimiento = self.fecha_nac.get()
        nombre_escuela = self.escuela.get()
        lugar_nacimiento = self.distrito.get()

        self.datos.loc[len(self.datos)] = [fecha_nacimiento, nombre_escuela, lugar_nacimiento]

        print(self.datos)

        bi.buscar_ingresante(fecha_nacimiento, nombre_escuela, lugar_nacimiento)

    def visualizar_grafico(self):
        selected_option = self.graficos_var.get()
        if selected_option == 'Tipo de Examen':
            dt.modalidad_examen()
        elif selected_option == 'Escuelas Profesionales':
            dt.grafico_escuela_general()
        elif selected_option == 'Escuelas Profesionales Top-3':
            dt.grafico_escuela_top3()
        elif selected_option == 'Escuelas Profesionales Menos Ingresantes':
            dt.grafico_escuela_bottom3()
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
        elif selected_option == 'Matriz de correlacion':
            self.matriz_de_correlacion()

    def matriz_de_correlacion(self):
        conteo_ingresantes = self.df.groupby(['MODALIDAD', 'DEPARTAMENTO_NACIMIENTO', 'PROVINCIA_NACIMIENTO', 'DISTRITO_NACIMIENTO']).size().reset_index(name='Cantidad')

        tabla_pivote = conteo_ingresantes.pivot_table(values='Cantidad', index=['DEPARTAMENTO_NACIMIENTO', 'PROVINCIA_NACIMIENTO', 'DISTRITO_NACIMIENTO'], columns='MODALIDAD', fill_value=0)

        matriz_correlacion = tabla_pivote.corr()

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', center=0, ax=ax)

        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
        ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    app = Interfaz()