import csv

# PROGRAMA USADO PARA CAMBIAR LA ETIQUETA DE IVAS

# debo haber ejecutado el primer script python: 3_cambiar_porcentaje.py

# Abrir el archivo CSV original y crear un archivo nuevo
with open('nuevo_ivas.csv', 'r', encoding='utf-8') as archivo_original, open('columnas_padre_hijo_productos.csv', 'w', newline='', encoding='utf-8') as archivo_nuevo:
        
    # Crear un objeto lector y escritor CSV
    lector_csv = csv.reader(archivo_original)
    escritor_csv = csv.writer(archivo_nuevo)
    print(lector_csv)

    # Leer la cabecera del archivo CSV original
    cabecera = next(lector_csv)
    print("cabecera: ", cabecera, type(cabecera))

    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append('categoria-producto-padre')
    print("\ncabecera 2:", cabecera)

    # Escribir la cabecera en el archivo nuevo
    escritor_csv.writerow(cabecera)
    contador = 0
    categorias_padre_e_hijo = []

    for i, fila in enumerate(lector_csv):

        valor_padre_hijo = fila[4] + '-->' +fila[15]

        if contador < 5000:
            print(f"#{i} valor_padre_hijo: ", valor_padre_hijo, type(valor_padre_hijo))

            print("\n",fila)
            print("categorias_padre: ", categorias_padre_e_hijo)

            if not valor_padre_hijo in categorias_padre_e_hijo:

                print("lo que contiene fila[4]: ", fila[4], type(fila[4]))
                categorias_padre_e_hijo.append(fila[4] + '-->' +fila[15])

                nueva_fila = fila + [fila[4] + '-->' +fila[15]]
                #print("\nnueva fila: ", nueva_fila)
                escritor_csv.writerow(nueva_fila)
                contador = contador + 1
                print("contador: ",contador)
