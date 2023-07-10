import csv

# PROGRAMA USADO PARA CAMBIAR LA ETIQUETA DE UNIDAD por unidades agregando una nueva columna 'Unidad de Medida'

# debo haber ejecutado el primer script python: 3_nuevo_formato_iva.py

# Abrir el archivo CSV original y crear un archivo nuevo
#luego cambio el csv 
with open('4_añadir_unidad_costo.csv', 'r', encoding='utf-8') as archivo_original, open('5_cambiar_etiqueta_unidad.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('Unidad de Medida')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    for fila in lector_csv:

        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + ["Unidades"]

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)