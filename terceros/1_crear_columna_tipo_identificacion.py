import csv

# PROGRAMA USADO PARA AÑADIR COLUMNA TIPO DE IDENTIFICACIÓN

# debo haber ejecutado el primer script python: 3_nuevo_formato_iva.py
#07-07-2023

# Abrir el archivo CSV original y crear un archivo nuevo
with open('terceros.csv', 'r', encoding='utf-8') as archivo_original, open('1_crear_columna_tipo_identificacion.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('tipo identificacion')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    for fila in lector_csv:

        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + ["NIT"]

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)