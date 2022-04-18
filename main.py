print('Bienvenido al programa! Identificate por favor')
nombre = input('Introduce tu nombre: ')
apellidos = input('Tus apellidos: ')
lugar = input('El lugar donde naciste: ')
edad = int(input('Tu edad: '))
texto = input('Algun comentario?: ')

print('-------------------------------------------------------------------------------------')
# Voy buscando palabras del comentario y cambiando
if texto.find('bien') != -1:
    print("El usuario ha dicho que "+texto.replace('bien', 'mal'))

elif texto.find('excelente') != -1:
    print("El usuario ha dicho que " + texto.replace('excelente', 'pésimo'))

elif texto.find('bueno') != -1:
    print("El usuario ha dicho que " + texto.replace('bueno', 'malo'))

arreglo = ['A Coruña', 'Barcelona', 'Kuala Lumpur', 'La Habana', 'Los Ángeles', 'Madrid', 'Tokio', 'Valencia', 'Vigo']

# Busco la ciudad que introducí antes y en caso de que no esté lanzo un mensaje
for pos in arreglo:
    if pos == lugar:
        print('Debes de vivir en '+pos)
    else:
        print('Vives en otra ciudad')


def mostrarEnPantalla():
    print ('-------------------------------------------------------------------------------------')
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


print('##### FIN DEL PROGRAMA #####')
