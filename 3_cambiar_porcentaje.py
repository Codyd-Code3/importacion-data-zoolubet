import csv

# PROGRAMA USADO PARA CAMBIAR LA ETIQUETA DE IVAS

# debo haber ejecutado el primer script python: 2_unir_descripcion.py

# Abrir el archivo CSV original y crear un archivo nuevo
with open('Producto_unir_Diseño_and_Unidad_referenciada.csv', 'r', encoding='utf-8') as archivo_original, open('nuevo_ivas.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('nuevo iva')

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)

    for fila in lector_csv:

        iva = []

        if fila[11] == '19':
            iva = ["IVA Ventas 19%"]

        elif fila[11] == '5':
            iva = ["IVA Ventas 5%"]
        elif fila[11] == '0':
            iva = ["sin iva"]

        # Mezclar las columnas que deseas combinar y agregarlas a la nueva fila
        nueva_fila = fila + iva

        # Escribir la nueva fila en el archivo nuevo
        escritor_csv.writerow(nueva_fila)