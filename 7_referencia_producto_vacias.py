import csv

# PROGRAMA USADO PARA AÑADIR UNA COLUMNA QUE ME MUESTRE LAS REFERENCIAS DE LOS PRODUCTOS EN CERO SI NO EXISTEN O ESTAN VACIOS

# ------------> Con este script, la columna que genere que en este caso es 'Nueva referencia producto' debo hacer la validacion
#en el siguiente script--------------------#


# Abrir el archivo CSV original y crear un archivo nuevo
#luego cambio la ruta del csv
with open('5_cambiar_etiqueta_unidad.csv', 'r', encoding='utf-8') as archivo_original, open('7_referencia_producto_vacias.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('Nueva referencia producto')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    barra= ''

    # Iterar por cada fila del archivo original
    for fila in lector_csv:
        
        if fila[2] == '':
            barra = '0'
        else:
            barra = fila[2]

        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + [barra]

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)