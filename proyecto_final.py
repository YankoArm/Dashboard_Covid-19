import csv
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Leer archivo CSV
with open('RecursoProyecto3.csv', 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv)
    datos = [fila for fila in lector_csv]  # Convertir a lista de diccionarios
    
    for fila in datos:
        fecha_str = fila['date']  # Extraemos la fecha como string
        fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")  # Convertimos a datetime
        dia_semana = fecha_obj.strftime("%A")  # Extraemos el nombre del día
        fila['dia_semana'] = dia_semana  # Guardamos el día de la semana en la fila

# calcular acumulados
def calcular_acumulados(grupo):
    acumulados = {
        'num_def': 0,
        'new_cases': 0,
        'num_hosp': 0,
        'num_uci': 0
    }
    for fila in grupo:
        acumulados['num_def'] += int(fila['num_def'])
        acumulados['new_cases'] += int(fila['new_cases'])
        acumulados['num_hosp'] += int(fila['num_hosp'])
        acumulados['num_uci'] += int(fila['num_uci'])
    return acumulados

# Agrupar datos por día de la semana y calcular acumulados
grupo_diasemana = {}
for fila in datos:
    dia_semana = fila['dia_semana']
    if dia_semana not in grupo_diasemana:
        grupo_diasemana[dia_semana] = []
    grupo_diasemana[dia_semana].append(fila)

# Agrupar datos por provincias y calcular acumulados
grupo_provincias = {}
for fila in datos:
    provincia = fila['province']
    if provincia not in grupo_provincias:
        grupo_provincias[provincia] = []
    grupo_provincias[provincia].append(fila)

# Calcular acumulados para cada grupo
acumulados_diasemana = {dia_semana: calcular_acumulados(grupo) for dia_semana, grupo in grupo_diasemana.items()}
acumulados_provincias = {provincia: calcular_acumulados(grupo) for provincia, grupo in grupo_provincias.items()}

# Guardar datos agrupados en un archivo TXT en formato JSON
with open('covid_data.json', 'w') as data_json:
    json.dump({
        'acumulados_por_dia': acumulados_diasemana,
        'acumulados_por_provincia': acumulados_provincias
    }, data_json, indent=4)  # formato legible

# Mostrar los acumulados por día de la semana
print("Acumulados por día de la semana:")
for diasemana, acumulados in acumulados_diasemana.items():
    print(f"\nDía: {diasemana}")
    print(f"  Defunciones: {acumulados['num_def']}")
    print(f"  Nuevos casos: {acumulados['new_cases']}")
    print(f"  Hospitalizados: {acumulados['num_hosp']}")
    print(f"  UCI: {acumulados['num_uci']}")

# Mostrar los acumulados por provincia
print("\nAcumulados por provincia:")
for provincia, acumulados in acumulados_provincias.items():
    print(f"\nProvincia: {provincia}")
    print(f"  Defunciones: {acumulados['num_def']}")
    print(f"  Nuevos casos: {acumulados['new_cases']}")
    print(f"  Hospitalizados: {acumulados['num_hosp']}")
    print(f"  UCI: {acumulados['num_uci']}")

# Funciones para cada gráfica (Ejercicio 2)
def defunciones_semana():
    dias = list(acumulados_diasemana.keys())
    defunciones = [acumulados['num_def'] for acumulados in acumulados_diasemana.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(dias, defunciones, color='red')
    plt.title('Defunciones por día de la semana')
    plt.xlabel('Día de la semana')
    plt.ylabel('Número de defunciones')
    plt.show()

def defunciones_provincias():
    provincias = list(acumulados_provincias.keys())
    defunciones = [acumulados['num_def'] for acumulados in acumulados_provincias.values()]

    plt.figure(figsize=(20, 10))
    plt.barh(provincias, defunciones, color='Green')
    plt.title('Defunciones por provincias')
    plt.ylabel('Provincia')
    plt.xlabel('Número de defunciones')
    plt.tight_layout()
    plt.show()

def nuevos_casos_semana():
    dias = list(acumulados_diasemana.keys())
    nuevos_casos = [acumulados['new_cases'] for acumulados in acumulados_diasemana.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(dias, nuevos_casos, color='red')
    plt.title('Nuevos casos por día de la semana')
    plt.xlabel('Día de la semana')
    plt.ylabel('Número de nuevos casos')
    plt.show()

def nuevos__casos_provincias():
    provincias = list(acumulados_provincias.keys())
    nuevos_casos = [acumulados['new_cases'] for acumulados in acumulados_provincias.values()]

    plt.figure(figsize=(20, 10))
    plt.barh(provincias, nuevos_casos, color='Green')
    plt.title('Nuevos casos por provincias')
    plt.ylabel('Provincia')
    plt.xlabel('Número de nuevos casos')
    plt.tight_layout()
    plt.show()

def hospitalizados_semana():
    dias = list(acumulados_diasemana.keys())
    hospitalizados = [acumulados['num_hosp'] for acumulados in acumulados_diasemana.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(dias, hospitalizados, color='red')
    plt.title('Hospitalizados por día de la semana')
    plt.xlabel('Día de la semana')
    plt.ylabel('Número de hospitalizados')
    plt.show()

def hospitalizados_provincia():
    provincias = list(acumulados_provincias.keys())
    hospitalizados = [acumulados['num_hosp'] for acumulados in acumulados_provincias.values()]

    plt.figure(figsize=(20, 10))
    plt.barh(provincias, hospitalizados, color='green')
    plt.title('Hospitalizados por provincia', fontsize=16)
    plt.xlabel('Número de hospitalizados')
    plt.ylabel('Provincias')
    plt.tight_layout()
    plt.show()

def uci_semana():
    dias = list(acumulados_diasemana.keys())
    uci = [acumulados['num_uci'] for acumulados in acumulados_diasemana.values()]

    plt.figure(figsize=(10, 5))
    plt.bar(dias, uci, color='red')
    plt.title('Pacientes en UCI por día de la semana')
    plt.xlabel('Día de la semana')
    plt.ylabel('Número de pacientes en UCI')
    plt.show()

def uci_provincia():
    provincias = list(acumulados_provincias.keys())
    uci = [acumulados['num_uci'] for acumulados in acumulados_provincias.values()]

    plt.figure(figsize=(20, 10))
    plt.barh(provincias, uci, color='green')
    plt.title('Pacientes en UCI por provincia')
    plt.ylabel('Provincias')
    plt.xlabel('Número de pacientes en UCI')
    plt.tight_layout()
    plt.show()

# Menú
while True:
    print("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Continuar al siguiente menú
    6 Salir""")
    
    opcion = input("Elige una opción (1-5): ")

    # Convertir la opción a un número entero
    try:
        opcion = int(opcion)
    except ValueError:
        print("Opción no válida. Por favor, ingresa un número del 1 al 5.")
        continue  # Volver al inicio

    # Ejecutar la opción seleccionada
    if opcion == 1:
        defunciones_semana()
        defunciones_provincias()
        print("Mostrando gráfica de Defunciones...")
    elif opcion == 2:
        nuevos_casos_semana()
        nuevos__casos_provincias()
        print("Mostrando gráfica de Casos...")
    elif opcion == 3:
        hospitalizados_semana()
        hospitalizados_provincia()
        print("Mostrando gráfica de Hospitalizados...")
    elif opcion == 4:
        uci_semana()
        uci_provincia()
        print("Mostrando gráfica de UCI...")
    elif opcion == 5:
        print("Continuando al siguiente menú...")
        break 
    elif opcion == 6:
        print("¡Gracias por usar el programa! ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 6.")

# Funciones para cada gráfica (Ejercicio 3)
def provincia_mas_defunciones():
    max_provincia = max(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_def'])
    max_defunciones = acumulados_provincias[max_provincia]['num_def']

    # Encontrar la provincia con el mínimo número de defunciones
    min_provincia = min(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_def'])
    min_defunciones = acumulados_provincias[min_provincia]['num_def']

    plt.figure(figsize=(8, 8))
    plt.pie([max_defunciones, sum(acumulados_provincias[p]['num_def'] for p in acumulados_provincias if p != max_provincia)], 
            labels=[max_provincia, 'Otras Provincias'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Provincia con más defunciones: {max_provincia}')
    plt.show()

    # Mostrar la información en la consola
    print("\nInformación adicional:")
    print(f"Provincia con más defunciones: {max_provincia} ({max_defunciones} defunciones)")
    print(f"Provincia con menos defunciones: {min_provincia} ({min_defunciones} defunciones)")

def provincia_mas_casos():
    max_provincia = max(acumulados_provincias, key=lambda p: acumulados_provincias[p]['new_cases'])
    max_casos = acumulados_provincias[max_provincia]['new_cases']

    # Encontrar la provincia con el mínimo número de casos
    min_provincia = min(acumulados_provincias, key=lambda p: acumulados_provincias[p]['new_cases'])
    min_casos = acumulados_provincias[min_provincia]['new_cases']

    plt.figure(figsize=(8, 8))
    plt.pie([max_casos, sum(acumulados_provincias[p]['new_cases'] for p in acumulados_provincias if p != max_provincia)], 
            labels=[max_provincia, 'Otras Provincias'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Provincia con más casos: {max_provincia}')
    plt.show()

    # Mostrar la información en la consola
    print("\nInformación adicional:")
    print(f"Provincia con más casos: {max_provincia} ({max_casos} casos)")
    print(f"Provincia con menos casos: {min_provincia} ({min_casos} casos)")

def provincia_mas_hospitalizados():
    max_provincia = max(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_hosp'])
    max_hospitalizados = acumulados_provincias[max_provincia]['num_hosp']

    # Encontrar la provincia con el mínimo número de hospitalizados
    min_provincia = min(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_hosp'])
    min_hospitalizados = acumulados_provincias[min_provincia]['num_hosp']

    plt.figure(figsize=(8, 8))
    plt.pie([max_hospitalizados, sum(acumulados_provincias[p]['num_hosp'] for p in acumulados_provincias if p != max_provincia)], 
            labels=[max_provincia, 'Otras Provincias'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Provincia con más hospitalizados: {max_provincia}')
    plt.show()

    # Mostrar la información en la consola
    print("\nInformación adicional:")
    print(f"Provincia con más hospitalizados: {max_provincia} ({max_hospitalizados} hospitalizados)")
    print(f"Provincia con menos hospitalizados: {min_provincia} ({min_hospitalizados} hospitalizados)")

def provincia_mas_uci():
    max_provincia = max(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_uci'])
    max_uci = acumulados_provincias[max_provincia]['num_uci']

    # Encontrar la provincia con el mínimo número de uci
    min_provincia = min(acumulados_provincias, key=lambda p: acumulados_provincias[p]['num_uci'])
    min_uci = acumulados_provincias[min_provincia]['num_uci']

    plt.figure(figsize=(8, 8))
    plt.pie([max_uci, sum(acumulados_provincias[p]['num_uci'] for p in acumulados_provincias if p != max_provincia)], 
            labels=[max_provincia, 'Otras Provincias'], autopct='%1.1f%%', startangle=140)
    plt.title(f'Provincia con más casos en UCI: {max_provincia}')
    plt.show()

    # Mostrar la información en la consola
    print("\nInformación adicional:")
    print(f"Provincia con más pacientes en UCI: {max_provincia} ({max_uci} pacientes en UCI)")
    print(f"Provincia con menos pacientes en UCI: {min_provincia} ({min_uci} pacientes en UCI)")

# Menú
while True:
    print("""¿Qué gráfica quieres visualizar?
    1. Provincia con más defunciones
    2. Provincia con más casos
    3. Provincia con más hospitalizados
    4. Provincia con más pacientes en UCI
    5. Salir""")
    
    opcion = input("Elige una opción (1-5): ")

    # Convertir la opción a un número entero
    try:
        opcion = int(opcion)
    except ValueError:
        print("Opción no válida. Por favor, ingresa un número del 1 al 5.")
        continue  # Volver al inicio

    # Ejecutar la opción seleccionada
    if opcion == 1:
        provincia_mas_defunciones()
    elif opcion == 2:
        provincia_mas_casos()
    elif opcion == 3:
        provincia_mas_hospitalizados()
    elif opcion == 4:
        provincia_mas_uci()
    elif opcion == 5:
        print("¡Gracias por usar el programa! ¡Hasta luego!")
        break 
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
