import csv

# PROGRAMA USADO PARA UNIR LAS COLUMNAS: Diseño , y Unidad referenciada

# debo haber ejecutado el primer script python: 1_unir_categorias_productos.py

# Abrir el archivo CSV original y crear un archivo nuevo
with open('Producto_unir_categorias_padrehijo.csv', 'r', encoding='utf-8') as archivo_original, open('Producto_unir_Diseño_and_Unidad_referenciada.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('descripcion (Notas Internas)')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    # Iterar por cada fila del archivo original
    for fila in lector_csv:
        
        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + [fila[14] + ' // ' + fila[17]]

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)