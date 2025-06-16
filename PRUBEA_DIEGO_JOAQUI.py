
def serva_zapatilla(reserva):
    if len(reserva) >= 20:
        print("se ha alcanzado el máximo de reservas")
        return reserva
    nombre = input("Ingrese su nombre: ")
    if nombre in reserva:
        print("Ya tiene una zapatilla reservada")
        return reserva
    codigo = input("Ingrese el código SECRETO DE RESERVA: ")
    if codigo != "EstoyEnListaDeReserva":
        print("El código  no es válido")
        return reserva
    reserva[nombre] = 1
    print(f"reserva exitosa para {nombre}")
    return reserva

def buscar_reserva(reserva):
    nombre = input("Ingrese su nombre: ")
    if nombre in reserva:
        print(f"se ha encontrado una reserva para {nombre}")
        
        vip = input("desea hacer una reserva VIP? (si/no): ").strip().lower()
        if vip == "si":
            reserva[nombre] = 2
            print("reserva VIP exitosa, ahora cuenta con 2 pares agendados ")
        else:
            print("reserva normal confirmada")
    else:
        print("no se ha encontrado una reserva para el nombre de: ", nombre)
    return reserva  
def cancelar_reserva(reserva):
    nombre = input("Ingrese su nombre: ")
    if nombre in reserva:
        del reserva[nombre]
        print(f"reserva cancelada para {nombre}")
    else:
        print(f"no se ha encontrado una reserva para el nombre de: {nombre}")
    return reserva      

def menu():
    reservas = {}  
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Cancelar reserva de zapatillas")
        print("4.- Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reservas = serva_zapatilla(reservas)
        elif opcion == "2":
            reservas = buscar_reserva(reservas)
        elif opcion == "3":
            reservas = cancelar_reserva(reservas)
        elif opcion == "4":
            print("Gracias por usar el sistema de reservas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

menu()