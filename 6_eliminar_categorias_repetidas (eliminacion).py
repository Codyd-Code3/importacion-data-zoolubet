import csv

# PROGRAMA USADO PARA PODER SACAR SOLAMENTE LOS GRUPOS Y SUB-GRUPOS QUE NO SE REPITEN DENTRO DEL ARCHIVO 
#----------- Esto con el fin de poder cargar estas categorias en el modelo de 'Categorias del Producto' ----------------- 

# debo haber ejecutado el primer script python: 3_nuevo_formato_iva.py

# Abrir el archivo CSV original y crear un archivo nuevo
with open('5_cambiar_etiqueta_unidad.csv', 'r', encoding='utf-8') as archivo_original, open('6_eliminar_categorias_repetidas (eliminacion).csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    #print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)
    #print("cabecera: ", cabecera, type(cabecera))

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('categoria-producto-padre-unicas')
    #print("\ncabecera 2:", cabecera)

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)
    contador = 0
    categorias_padre_e_hijo = []

    for i, fila in enumerate(lector_csv):

        valor_padre_hijo = fila[4] + '-->' +fila[15]

        #el contador lo utilizo más para poder hacer pruebas
        if contador < 5000:
            #print(f"#{i} valor_padre_hijo: ", valor_padre_hijo, type(valor_padre_hijo))

            #print("\n",fila)
            #print("categorias_padre: ", categorias_padre_e_hijo)

            if not valor_padre_hijo in categorias_padre_e_hijo:

                #print("lo que contiene fila[4]: ", fila[4], type(fila[4]))
                if fila[15] != '':
                    categorias_padre_e_hijo.append(fila[4] + '-->' +fila[15])

                    nueva_fila = fila + [fila[4] + '-->' +fila[15]]
                    #print("\nnueva fila: ", nueva_fila)
                    escritor_csv.writerow(nueva_fila)
                    contador = contador + 1
                else:
                    print(f"el subgrupo en el producto {fila[0]} está vacio, no se tiene en cuenta entonces")
                    #print("contador: ",contador)
