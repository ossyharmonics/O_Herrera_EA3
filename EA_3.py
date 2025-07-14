reservas = []
max_reservas = 20
frase_secreta = "EstoyEnListaDeReserva"

def mostrar_menu():
    print("***************MENU PRINCIPAL****************")
    print("Bienvenido al Tótem de Auto-Atención de \nRESERVASTRIKE. Por favor ingresa la opción \ndeseada.\n")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Ver stock de reservas")
    print("4.- Salir")
    print("\n*********************************************")
    
    
def reservar_zapatillas():
    try:
        if len(reservas) >= max_reservas:
            print("Ya se ha alcanzado el máximo de reservas.")
            return
        nombre = input("Ingrese su nombre: ").strip().capitalize()
        if nombre == "":
            print("Debe ingresar un nombre.")
        if any(reserva["nombre"] == nombre for reserva in reservas):
            print("El nombre ingresado ya ha sido asociado a una reserva.")
            return
    
        clave = input("Ingrese la clave secreta para realizar reserva.\nDEBES RESPETAR MAYÚSCULAS Y MINÚSCULAS.\n").strip()
        if clave != frase_secreta:
            print("Lo sentimos. La clave secreta no es correcta \nNo se ha podido completar la reserva.")
            return
        reservas.append({"nombre":nombre, "vip":"No", "cantidad":1})
        print(f"\n{nombre}, has realizado la reserva correctamente. Gracias por preferirnos.\n")
    except Exception as e:
        print(f"Ha ocurrido un error. No se ha realizado la reserva.{e}")
        

def buscar_reserva():
    try:
        nombre = input("Ingrese el nombre con el cuál se registró la reserva.\n").strip().capitalize()
        
        if nombre == "":
            print("'Nombre' no puede estar vacío.")
            return
        
        for reserva in reservas:
            if reserva['nombre'] == nombre:
                print(f"Reserva encontrada: {nombre}. \nCantidad reservada: {reserva['cantidad']}")
                if reserva["vip"].lower() == "no":
                    respuesta = input("¿Desea pagar un adicional para una reserva VIP.\n podrá reservar 2 pares? (s/n): ").lower()
                    if respuesta == "s":
                        total_reservas_actual = sum(r["cantidad"] for r in reservas)
                        if total_reservas_actual + 1 <= max_reservas:
                            reserva["vip"] = "si"
                            reserva["cantidad"] = 2
                            print("¡Has actualizado a VIP! pares reservados: 2 \n\n")
                        else:
                            print("No hay stock suficiente para reserva VIP.") 
                return

        print(f"Lo sentimos. {nombre} no tiene reservas registradas.\n\n")        
    except Exception as e:
        print(f"Ha ocurrido un error. No hemos podido consultar la reserva. {e}")
        
        
def ver_stock():
    try:
        total_reservas = sum(i["cantidad"] for i in reservas)
        restante = max_reservas - total_reservas
        print(f"\nTotal de pares de zapatillas reservadas: {total_reservas}")
        print(f"Pares disponibles para reservar: {restante}\n\n")
    except Exception as e:
        print(f"Ocurrió un error al mostrar el stock: {e}")
        

def main():
    while True:
        try:
            mostrar_menu()
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                reservar_zapatillas()
            elif opcion == 2:
                buscar_reserva()
            elif opcion == 3:
                ver_stock()
            elif opcion == 4:
                print("Programa terminado. ¡Hasta pronto!")
                break
            else:
                print("\nLa opción ingresada no está permitida.\n\n")               
        except ValueError:
            print("\nDebes ingresar una opción válida.\n\n")
main()