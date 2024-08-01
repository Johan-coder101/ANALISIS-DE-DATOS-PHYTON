import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

documento = 'DATA_INGRESANTES_SIN_ACENTOS.csv'
df = pd.read_csv(documento)
total_datos = 6536

def cargar_datos(documento):
    return pd.read_csv(documento)

def modalidad_examen():
    modalidad_counts = df['MODALIDAD'].value_counts()
    umbral = total_datos * 0.10
    modalidades_principales = modalidad_counts[modalidad_counts >= umbral]
    modalidades_principales['Otros'] = modalidad_counts[modalidad_counts < umbral].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(modalidades_principales, labels=modalidades_principales.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
    plt.legend(labels=modalidades_principales.index, loc='lower right')
    plt.title('Distribución de Modalidad de Examen')
    plt.show()

def grafico_escuela_general():
    escuela_counts = df['ESCUELA DE PROFESIONAL'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.countplot(x='ESCUELA DE PROFESIONAL', data=df, palette='viridis', order=escuela_counts.index)
    plt.title('Distribución de Escuela Profesional de Ingresantes')
    plt.xlabel('Escuela Profesional')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def grafico_escuela_top3():
    top_escuelas = df['ESCUELA DE PROFESIONAL'].value_counts().nlargest(3).index
    top_escuela_counts = df[df['ESCUELA DE PROFESIONAL'].isin(top_escuelas)]['ESCUELA DE PROFESIONAL'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(top_escuela_counts, labels=top_escuela_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
    plt.title('Top 3 Escuelas con Más Ingresantes')
    plt.show()

def grafico_escuela_bottom3():
    bottom_escuelas = df['ESCUELA DE PROFESIONAL'].value_counts().nsmallest(3).index
    bottom_escuela_counts = df[df['ESCUELA DE PROFESIONAL'].isin(bottom_escuelas)]['ESCUELA DE PROFESIONAL'].value_counts()
    
    plt.figure(figsize=(8, 8))
    plt.pie(bottom_escuela_counts, labels=bottom_escuela_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
    plt.title('Top 3 Escuelas con Menos Ingresantes')
    plt.show()

def grafico_fechas_de_nacimiento():
    df['F_NACIMIENTO'] = pd.to_datetime(df['F_NACIMIENTO'], format='%Y%m%d', errors='coerce')
    df['AÑO_NACIMIENTO'] = df['F_NACIMIENTO'].dt.year
    df = df.dropna(subset=['AÑO_NACIMIENTO'])

    plt.figure(figsize=(12, 6))
    sns.countplot(x='AÑO_NACIMIENTO', data=df, palette='viridis')
    plt.title('Distribución de Años de Nacimiento de Ingresantes')
    plt.xlabel('Año de Nacimiento')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def pais_de_nacimiento():
    plt.figure(figsize=(12, 6))
    sns.countplot(x='PAIS_NACIMIENTO', data=df, palette='viridis', order=df['PAIS_NACIMIENTO'].value_counts().index)
    plt.title('Distribución de Ingresantes por País de Nacimiento')
    plt.xlabel('País de Nacimiento')
    plt.ylabel('Cantidad')
    plt.show()

def visualizar_por_departamento():
    plt.figure(figsize=(15, 6))
    sns.countplot(x='DEPARTAMENTO_NACIMIENTO', data=df, palette='viridis', order=df['DEPARTAMENTO_NACIMIENTO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Departamento de Nacimiento')
    plt.xlabel('Departamento de Nacimiento')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def visualizar_por_provincia():
    plt.figure(figsize=(15, 6))
    sns.countplot(x='PROVINCIA_NACIMIENTO', data=df, palette='viridis', order=df['PROVINCIA_NACIMIENTO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Provincia de Nacimiento')
    plt.xlabel('Provincia de Nacimiento')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def visualizar_top_10_distritos():
    top_distritos = df['DISTRITO_NACIMIENTO'].value_counts().nlargest(10).index
    df_top_distritos = df[df['DISTRITO_NACIMIENTO'].isin(top_distritos)]

    plt.figure(figsize=(15, 6))
    sns.countplot(x='DISTRITO_NACIMIENTO', data=df_top_distritos, palette='viridis', order=top_distritos)
    plt.title('Distribución de Ingresantes por Distrito de Nacimiento (Top 10)')
    plt.xlabel('Distrito de Nacimiento')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def estado_civil():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='ESTADO_CIVIL', data=df, palette='viridis', order=df['ESTADO_CIVIL'].value_counts().index)
    plt.title('Distribución de Ingresantes por Estado Civil')
    plt.xlabel('Estado Civil')
    plt.ylabel('Cantidad')
    plt.show()

def anio_egreso():
    plt.figure(figsize=(12, 6))
    sns.countplot(x='AÑO_EGRESO', data=df, palette='viridis', order=df['AÑO_EGRESO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Año de Egreso')
    plt.xlabel('Año de Egreso')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.show()

def tipo_de_colegio():
    tipo_colegio_counts = df['TIPO_COLEGIO'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(tipo_colegio_counts, labels=tipo_colegio_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('viridis'))
    plt.title('Distribución de Ingresantes por Tipo de Colegio')
    plt.show()

def colegio_del_ingresante():
    plt.figure(figsize=(12, 6))
    sns.countplot(x='NOMBRE_COLEGIO', data=df, palette='viridis', order=df['NOMBRE_COLEGIO'].value_counts().index[:10])
    plt.title('Distribución de Ingresantes por Nombre del Colegio (Top 10)')
    plt.xlabel('Nombre del Colegio')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def departamentos_con_mas_ingresantes():
    top_departamentos = df['DEPARTAMENTO_COLEGIO'].value_counts().nlargest(5).index

    plt.figure(figsize=(15, 6))
    sns.countplot(x='DEPARTAMENTO_COLEGIO', data=df[df['DEPARTAMENTO_COLEGIO'].isin(top_departamentos)], palette='viridis', order=top_departamentos)
    plt.title('Top 5 Departamentos del Colegio con Más Ingresantes')
    plt.xlabel('Departamento del Colegio')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def provincias_con_mas_ingresantes():
    top_provincias = df['PROVINCIA_COLEGIO'].value_counts().nlargest(10).index

    plt.figure(figsize=(15, 6))
    sns.countplot(x='PROVINCIA_COLEGIO', data=df[df['PROVINCIA_COLEGIO'].isin(top_provincias)], palette='viridis', order=top_provincias)
    plt.title('Top 10 Provincias del Colegio con Más Ingresantes')
    plt.xlabel('Provincia del Colegio')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def distritos_con_mas_ingresantes():
    top_distritos = df['DISTRITO_COLEGIO'].value_counts().nlargest(10).index

    plt.figure(figsize=(15, 6))
    sns.countplot(x='DISTRITO_COLEGIO', data=df[df['DISTRITO_COLEGIO'].isin(top_distritos)], palette='viridis', order=top_distritos)
    plt.title('Top 10 Distritos del Colegio con Más Ingresantes')
    plt.xlabel('Distrito del Colegio')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def estado_biometrico():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='ESTADO_BIOMETRICO', data=df, palette='viridis', order=df['ESTADO_BIOMETRICO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Estado Biometrico')
    plt.xlabel('Estado Biometrico')
    plt.ylabel('Cantidad')
    plt.show()

def genero():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='GENERO', data=df, palette='viridis', order=df['GENERO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Género')
    plt.xlabel('Género')
    plt.ylabel('Cantidad')
    plt.show()

def ingresantes_por_discapacidad():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='DISCAPACIDAD', data=df, palette='viridis', order=df['DISCAPACIDAD'].value_counts().index)
    plt.title('Distribución de Ingresantes con Discapacidad')
    plt.xlabel('Discapacidad')
    plt.ylabel('Cantidad')
    plt.show()

def tipo_colegio_fiscal_privado():
    plt.figure(figsize=(8, 6))
    sns.countplot(x='TIPO_COLEGIO', data=df, palette='viridis', order=df['TIPO_COLEGIO'].value_counts().index)
    plt.title('Distribución de Ingresantes por Tipo de Colegio')
    plt.xlabel('Tipo de Colegio')
    plt.ylabel('Cantidad')
    plt.show()

def edad():
    df['EDAD'] = 2024 - df['AÑO_NACIMIENTO']
    plt.figure(figsize=(12, 6))
    sns.histplot(data=df, x='EDAD', bins=30, kde=True, color='purple')
    plt.title('Distribución de Edades de Ingresantes')
    plt.xlabel('Edad')
    plt.ylabel('Cantidad')
    plt.show()

def ingresantes_por_tipo_discapacidad():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='TIPO_DISCAPACIDAD', data=df, palette='viridis', order=df['TIPO_DISCAPACIDAD'].value_counts().index)
    plt.title('Distribución de Ingresantes por Tipo de Discapacidad')
    plt.xlabel('Tipo de Discapacidad')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=90)
    plt.show()

def visualizar_ingresantes_por_region():
    region_counts = df['REGION'].value_counts()
    plt.figure(figsize=(12, 6))
    sns.barplot(x=region_counts.index, y=region_counts.values, palette='viridis')
    plt.title('Distribución de Ingresantes por Región')
    plt.xlabel('Región')
    plt.ylabel('Cantidad')
    plt.xticks(rotation=45)
    plt.show()

def grafico_puntajes_maximos_primeros():
    # Obtener los puntajes máximos por carrera y ordenar de mayor a menor
    puntajes_maximos = df.groupby('ESCUELA DE PROFESIONAL')['PUNTAJE_TOTAL'].max().sort_values(ascending=False)
    primeros_puntajes = puntajes_maximos.head(33)

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 10))
    sns.barplot(x=primeros_puntajes.values, y=primeros_puntajes.index, palette='viridis')
    for index, value in enumerate(primeros_puntajes):
        plt.text(value + 1, index, str(round(value, 2)), va='center')
    plt.title('Primeros 33 Puntajes Máximos por Carrera')
    plt.xlabel('Puntaje Máximo')
    plt.ylabel('Carrera')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_puntajes_maximos_ultimos():
    # Obtener los puntajes máximos por carrera y ordenar de mayor a menor
    puntajes_maximos = df.groupby('ESCUELA DE PROFESIONAL')['PUNTAJE_TOTAL'].max().sort_values(ascending=False)
    ultimos_puntajes = puntajes_maximos.tail(33)

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 10))
    sns.barplot(x=ultimos_puntajes.values, y=ultimos_puntajes.index, palette='viridis')
    for index, value in enumerate(ultimos_puntajes):
        plt.text(value + 1, index, str(round(value, 2)), va='center')
    plt.title('Últimos 33 Puntajes Máximos por Carrera')
    plt.xlabel('Puntaje Máximo')
    plt.ylabel('Carrera')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def matriz_de_correlacion():
    conteo_ingresantes = df.groupby(['MODALIDAD', 'DEPARTAMENTO_NACIMIENTO', 'PROVINCIA_NACIMIENTO', 'DISTRITO_NACIMIENTO']).size().reset_index(name='Cantidad')

# Crear una tabla pivote para preparar los datos para la matriz de correlación
    tabla_pivote = conteo_ingresantes.pivot_table(values='Cantidad', index=['DEPARTAMENTO_NACIMIENTO', 'PROVINCIA_NACIMIENTO', 'DISTRITO_NACIMIENTO'], columns='MODALIDAD', fill_value=0)

# Calcular la matriz de correlación
    matriz_correlacion = tabla_pivote.corr()

# Visualizar la matriz de correlación usando seaborn y matplotlib con barras de desplazamiento
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm', center=0, ax=ax)

# Configurar barras de desplazamiento
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

# Hacer el gráfico desplazable
    plt.tight_layout()
    plt.show()