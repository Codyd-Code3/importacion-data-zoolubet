import csv

# ESTE SCRIPT GENERA UN ARCHIVO EN EXCEL CON LAS REFERENCIAS QUE NO ESTAN REPETIDAS EN EL ARCHIVO DE EXCEL ELIMINANDOLAS y
#generando entonces un archivo con los codigos de referencia productos que no estan repetidos!!!
# ------------- con este script soluciono el problema de que hayan registros con la misma referencia del producto ------------


# Abrir el archivo CSV original y crear un archivo nuevo
#luego cambio la ruta del csv

productos_repetidos = []

with open('7_referencia_producto_vacias.csv', 'r', encoding='utf-8') as archivo_original, open('8_2_sin_referencias_repetidas_0.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)
    #print("cabecera: ", cabecera, type(cabecera))

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('referencia producto - primera vez')
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

            #si el valor de la referencia no está en la lista entonces lo agrega,
            if not valor_referencia in referencias_productos:
                referencias_productos.append(fila[24])

                nueva_fila = fila + [fila[24]]
                #print("\nnueva fila: ", nueva_fila)
                escritor_csv.writerow(nueva_fila)
                contador = contador + 1
            else:
                #debe volver a leer todos los registros de nuevo y buscar ese valor para poder eliminarlo
                #print(f"el valor del producto de referencia {fila[24]} se está repitiendo")
                productos_repetidos.append(fila[24])

#print("\ncodigo referencia productos repetidos: ", productos_repetidos)        
            #si el valor de la referencia ya está en la lista entonces ahora si lo construye, porque quiere decir que 
            #pertenece al grupo de los que se repiten
            #else:
                
with open('8_2_sin_referencias_repetidas_0.csv', 'r', encoding='utf-8') as archivo_original, open('8_2_sin_referencias_repetidas.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)
    #print("cabecera: ", cabecera, type(cabecera))

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('referencia producto - segunda vez')
    #print("\ncabecera 2:", cabecera)

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)
    contador = 0
    #referencias_productos = []
    productos_repetidos_2 = []
    

    for i, fila in enumerate(lector_csv):

        valor_referencia = fila[24]

        #el contador lo utilizo más para poder hacer pruebas
        if contador < 5000:
            #print(f"#{i} valor de la referencia: ", valor_referencia, type(valor_referencia))

            #print("\n",fila)
            #print("valor del arreglo: ", productos_repetidos)

            #si el valor de la referencia no está en la lista entonces lo agrega,
            if not valor_referencia in productos_repetidos:
                productos_repetidos.append(fila[24])

                nueva_fila = fila + [fila[24]]
                #print("\nnueva fila: ", nueva_fila)
                escritor_csv.writerow(nueva_fila)
                contador = contador + 1
            else:
                #debe volver a leer todos los registros de nuevo y buscar ese valor para poder eliminarlo
                #print(f"el valor del producto de referencia {fila[24]} se está repitiendo")
                productos_repetidos_2.append(fila[24])

print("\ncodigo referencia productos repetidos: ", productos_repetidos_2)  