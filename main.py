def identificarse():
    print('Bienvenido al programa! Identificate por favor')
    nombre = input('Introduce tu nombre: ')
    apellidos = input('Tus apellidos: ')
    lugar = input('El lugar donde naciste: ')
    edad = int(input('Tu edad: '))
    texto = input('Algun comentario?: ')

    print('-------------------------------------------------------------------------------------')
    # Voy buscando palabras del comentario y cambiando
    if texto.find('bien') != -1:
        print("El usuario ha dicho que " + texto.replace('bien', 'mal'))

    elif texto.find('excelente') != -1:
        print("El usuario ha dicho que " + texto.replace('excelente', 'pésimo'))

    elif texto.find('bueno') != -1:
        print("El usuario ha dicho que " + texto.replace('bueno', 'malo'))

    arreglo = ['A Coruña', 'Barcelona', 'Kuala Lumpur', 'La Habana', 'Los Ángeles', 'Madrid', 'Tokio', 'Valencia',
               'Vigo']

    diccionarioCiudades = {
        "A Coruña": "Ciudad muy fría y ubicada en el norte de Galicia",
        "Barcelona": "Ciudad capital de Cataluña y segunda más poblada de España",
        "Kuala Lumpur": "Ciudad del este de Asia",
        "La Habana": "Capital de Cuba y protagonista de Cuando Salí de la Habana",
        "Madrid": "Capital de España y de Ministerios",
        "Tokio": "Capital de Japón",
        "Valencia": "Tierra de Naranjas",
        "Vigo": "La mejor ciudad del mundo!"
    }
    encontrado = False
    # Busco la ciudad que introducí antes y en caso de que no esté lanzo un mensaje
    for pos in arreglo:
        if pos == lugar:
            print('Debes de vivir en ' + pos)
            print(diccionarioCiudades[lugar])
            encontrado = True;
        else:
            continue

    if encontrado == False:
        print('No hemos encontrado donde vives')

    def mostrarEnPantalla():
        print('-------------------------------------------------------------------------------------')
        print('Hola, su nombre es ' + nombre + ' ' + apellidos + ' y vive en ' + lugar + ', además tiene ' + str(
            edad) + ' años\n');

    mostrarEnPantalla()

    if edad < 30:
        print('Tienes menos de 30 años, tienes toda la vida por delante amigo!')
    else:
        print('Que mayor eres joer')

    numero = 0
    while numero != 2:
        print('########')
        print('########')
        print('########')
        numero = int(input('Pulse el numero mágico para continuar (del 1 al 10)'))
        # De los números hasta que dé con el número mágico me mantendré en el bucle
        if numero != 2:
            print('Buuuuuuuu ese no es el número, prueba otra vez!')
        if numero == 5:
            print('El if no hace nada!')
            continue
        else:
            print('Enhorabuena campeón!')

        print('########')
        print('########')
        print('########')


def cifrarTextos():
    archivo = open('contenido.txt', 'a')
    archivo.write('Prueba de guardado en el archivo')
    archivo.close()


def mostrarMenu():
    print("Bienvenido al programa")
    print("0 - Salir")
    print("1 - Identificate")
    print("2 - Cifra archivos")
    op = int(input('Elija una opcion: '))
    return op


while mostrarMenu() != 0:

    if mostrarMenu() == 1:
        identificarse()

    elif mostrarMenu() == 2:
        cifrarTextos()

    elif mostrarMenu() == 0:
        print("Gracias por usar el programa")

    else:
        print('Opcion invalida')
