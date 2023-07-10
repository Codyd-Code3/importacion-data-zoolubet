import csv

# ESTE SCRIPT GENERA LAS REFERENCIAS REPETIDAS QUE HAY EN EL ARCHIVO DE EXCEL
# ------------ ENTREGAR A DIEGO ---------------

# Abrir el archivo CSV original y crear un archivo nuevo
#luego cambio la ruta del csv
with open('7_referencia_producto_vacias.csv', 'r', encoding='utf-8') as archivo_original, open('Productos con referencia del producto repetida.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)
    #print("cabecera: ", cabecera, type(cabecera))

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('referencia producto')
    #print("\ncabecera 2:", cabecera)

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)
    contador = 0
    referencias_productos = []

    for i, fila in enumerate(lector_csv):

        valor_referencia = fila[24]

        #el contador lo utilizo más para poder hacer pruebas
        if contador < 5000:
            #print(f"#{i} valor de la referencia: ", valor_referencia, type(valor_referencia))

            #print("\n",fila)
            #print("valor del arreglo: ", referencias_productos)

            if not valor_referencia in referencias_productos:
                referencias_productos.append(fila[24])
            else:
                nueva_fila = fila + [fila[24]]
                #print("\nnueva fila: ", nueva_fila)
                escritor_csv.writerow(nueva_fila)
                contador = contador + 1
