''' Esta el desarrollo del ejercicio que evalúa las 
competencias requeridas para aprobar el Exámen Transversal
el cual tiepe una ponderación del 50% del semestre'''

mascotas = {
    "A321" : ["Ainara", "Perro", 9, "Quiltro"],
    "A322" : ["Kenai", "Perro", 2, "Quiltro"],
    "A323" : ["Miku", "Gato", 1, "Nebelung"],
    "A324" : ["Almendra", "Gato", 7, "Carey"],
    "A325" : ["Matilda", "Gato", 12, "Carey"],
    "A326" : ["Fito", "Gato", 5, "Quiltro"]
}
fichas = {
    "A321" : [25000, 5],
    "A322" : [32000, 2],
    "A323" : [31000, 2],
    "A324" : [22000, 1],
    "A325" : [27000, 0],
    "A326" : [35000, 1]
}
def mostrar_menu():
    print("*** MENÚ PRINCIPAL ***")
    print("1. Fichas por especie")
    print("2. Búsqueda por rango de precio")
    print("3. Actualizar precio de atención")
    print("4. Salir")

def mostrar_ficha(especie):
    encontrados: False
    for clave, datos in mascotas.items():
        if especie == datos[1]:
            nombre = datos[0]
            valor, consultas = fichas[clave]
            print(f"Nombre: {nombre} - ID: {clave}\nValor consultas: {valor}\nConsultas disponibles: {consultas}")
            encontrados = True
    return encontrados

def buscar_precio(precio_min, precio_max):
    encontrados = False
    for clave, datos in fichas.items():
        if precio_min <= datos[0] <= precio_max and datos[1] > 0:
            nombre = mascotas[clave]
            valor, consultas = fichas[clave]
            print(f"Nombre: {nombre[0]} - ID: {clave}\nValor consultas: {valor}\nConsultas disponibles: {consultas}")
            encontrados = True
    return encontrados

def modificar_precio(codigo, nuevo_precio):
    if codigo in fichas:
        fichas[codigo][0] = nuevo_precio
        print("Precio actualizado")
        return True
    else:
        print("Precio no actualizado.")
        return False

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("ingrese la opción a elegir: "))
            if opcion == 1:
                especie = input("Ingrese la especie a buscar: (Perro/Gato)").capitalize()
                if not mostrar_ficha(especie):
                    ("Especie no encontrada.")
            elif opcion == 2:
                while True:
                    try:    
                        precio_min = int(input("Ingrese el rango mínimo: "))
                        precio_max = int(input("Ingrese el rango máximo: "))
                        
                    except ValueError:
                        print("Debe ingresar valores enteros")
                        continue
                    if not buscar_precio(precio_min, precio_max):
                        print("Rango no encontrado.")
                        break
                    break
                    
            elif opcion == 3:
                while True:
                    codigo = input("Ingrese el código del paciente: ")
                    if not any(clave == codigo for clave in fichas):
                        print("No hay coicidencias.")
                        continue
                    try:
                        nuevo_precio = int(input("Ingrese nuevo precio: "))
                    except ValueError:
                        print("Debe ingresar valores enteros.")
                        continue
                    modificar_precio(codigo,nuevo_precio)
                    seguir = input("Desea realizar otra modificación? (si/no)").lower()
                    if seguir != "si":
                        break
            elif opcion == 4:
                print("Programa terminado.")
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Debe ingresar un número válido.")
main()