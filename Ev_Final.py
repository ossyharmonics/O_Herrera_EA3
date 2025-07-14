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
    encontrados = False
    print(f"Resultados para búsqueda {especie}:")
    for clave, datos in mascotas.items():
        if datos[1] == especie:
            nombre = datos[0]
            valor, consulta = fichas[clave] 
            print(f"Nombre: {nombre}, ID: {clave}\nValor de la consulta: {valor}\nConsultas disponibles: {consulta}")
            encontrados = True
    return encontrados

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                especie = input("Ingrese la especie que desea buscar (ej: 'Perro'/'Gato')").capitalize()
                if not mostrar_ficha(especie):
                    print("No hay coincidencias")
        except ValueError:
            print("Ingrese un número válido.")
main()