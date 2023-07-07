import csv

# PROGRAMA USADO PARA UNIR LAS COLUMNAS: Grupo , y sub-grupo --> Con el fin de crear la columna 'Categorias Padre-hijo'
#07-07-2023

# Abrir el archivo CSV original y crear un archivo nuevo
with open('Productos_original.csv', 'r', encoding='utf-8') as archivo_original, open('1_unir_categorias_productos.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('categoria padre-hijo')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    barra= ''

    # Iterar por cada fila del archivo original
    for fila in lector_csv:
        
        if fila[15] == '':
            barra = 'sin valor'
        else:
            barra = fila[4] + ' / ' + fila[15]

        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + [barra]

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)