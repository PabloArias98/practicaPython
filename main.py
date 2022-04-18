# Inicializamos
nombre = 'Celestino'
apellidos = 'Casal'
lugar = 'Tudela Veguin'
edad = 31
texto = "Julian Muñoz Cabezacobo"


def imprimirenPantalla():
    print('Hola, su nombre es ' + nombre + ' ' + apellidos + ' y vive en ' + lugar + ', además tiene ' + str(
        edad) + ' años\n');
    print(texto)


def multiplicarNumeros(a, b):
    return a * b


def darValores(nombre, apellidos, lugar, edad):
    print('Hola, su nombre es ' + nombre + ' ' + apellidos + ' y vive en ' + lugar + ', además tiene ' + str(
    edad) + ' años\n');

nombre = "Juan Ramón"

imprimirenPantalla()

darValores('Jose', 'Souto', 'Chapela', 50)

imprimirenPantalla()

if edad < 30:
    print('Tienes menos de 30 años')
else:
    print('Que mayor eres')

comentarios = input('Deja tus comentarios: ')
nacional = input('Eres nacional?: ')
edad = int(input('Introduce tu edad: '))

esMayorEdad = edad >= 18
esNacional = nacional == 'Si' or nacional == "si" or nacional == "SI"
esValido = esMayorEdad and esNacional

# en las operaciones aritméticas para saber si un número es par hacemos X % 2 == 0
print('Tus comentarios son: ' + comentarios)
print('Edad del usuario: ' + str(edad))

if esValido:
    print('Si')
else:
    print('Pertenece a sus padres')

a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))

print(str(multiplicarNumeros(a, b)))

print('##### FIN DEL PROGRAMA #####')
