def mostrar_cartelera(cartelera):
    print(" Peliculas Disponible ")
    for i, (pelicula, precio) in enumerate(cartelera.items(), 1):
        print(f"{i}. {pelicula} - ${precio}")

def procesar_compra():
    cartelera = {
        "Avengers": 15000,
        "Super Mario Bros": 12000,
        "Oppenheimer": 18000,
        "Spider-Man": 14000
    }
    
    salas = ("Sala 1 (2D)", "Sala 2 (3D)", "Sala 3 (IMAX)")
    
    historial_compras = []

    while True:
        try:
            mostrar_cartelera(cartelera)
            
            opcion = int(input("Seleccione el número de la película (o 0 para salir): "))
            
            if opcion == 0:
                break
            peliculas_lista = list(cartelera.keys())
            pelicula_seleccionada = peliculas_lista[opcion - 1]
            precio_unitario = cartelera[pelicula_seleccionada]
            
            cantidad = int(input(f"¿Cuántas boletas desea para '{pelicula_seleccionada}'?: "))
            
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")

            total = cantidad * precio_unitario
            compra = {
                "pelicula": pelicula_seleccionada,
                "cantidad": cantidad,
                "total": total
            }
            historial_compras.append(compra)

            print(f"\n Compra exitosa: {cantidad} boleta(s) para {pelicula_seleccionada}.")
            print(f"Total a pagar: ${total}")
            print(f"Ubicación: {salas[0]}") 

        except ValueError as e:
            print(f" Error de entrada: Asegúrate de ingresar un número válido. ({e})")
        except IndexError:
            print(" Error: Esa película no existe en la lista.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    print("Gracias por tu compra, disfruta la funcion")
    procesar_compra()
        


    
 
