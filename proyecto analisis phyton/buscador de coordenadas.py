import pandas as pd
from geopy.geocoders import Nominatim
import time
import sys

# Función para obtener coordenadas de un distrito
def obtener_coordenadas(distrito):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = None
    retries = 0
    while retries < 3:
        try:
            location = geolocator.geocode(f"{distrito}, Perú", timeout=10)
            break
        except Exception as e:
            retries += 1
            print(f"Error al obtener coordenadas para '{distrito}': {e}", file=sys.stderr)
            time.sleep(5)  # Espera antes de reintentar
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Leer archivo Excel
file_path_excel = 'distritos_coordenadas.csv'
df = pd.read_csv(file_path_excel)

# Obtener distritos únicos
distritos_unicos = df['DISTRITO_NACIMIENTO'].unique()

# Crear una lista para almacenar distritos y coordenadas
coordenadas = []

# Obtener coordenadas para cada distrito
for distrito in distritos_unicos:
    lat, lon = obtener_coordenadas(distrito)
    coordenadas.append({'distrito': distrito, 'lat': lat, 'lon': lon})
    time.sleep(2)  # Aumentamos el tiempo de espera a 2 segundos

# Crear DataFrame a partir de la lista de coordenadas
df_coordenadas = pd.DataFrame(coordenadas)

# Guardar coordenadas en un archivo CSV
output_file = 'distritos_coordenadas_actualizado.csv'
df_coordenadas.to_csv(output_file, index=False)

print(f"Coordenadas guardadas en {output_file}")