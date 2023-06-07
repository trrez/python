# Actualizar valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
print(x)

estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)

directorio_deportes['fútbol'][0] = 'Andres'
print(directorio_deportes['fútbol'])

z[0]['y'] = 30
print(z)

# Iterar a través de una lista de diccionarios
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(estudiantes):
    for estudiante in estudiantes:
        for clave, valor in estudiante.items():
            print(f"{clave} - {valor}", end=", ")
        print()


iterateDictionary(estudiantes)


# Obtener valores de una lista de diccionarios
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterate_dictionary2(key_name, list):
    for i in range(0, len(list)):

        for key, val in list[i].items():
            if key == key_name:
                print(val)


iterate_dictionary2('name', estudiantes)
iterate_dictionary2('last_name', estudiantes)

# Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for x in some_dict:
        print('---------------- \n', len(some_dict[x]), x.upper(), '\n')
        for y in some_dict[x]:
            print(y)


printInfo(dojo)
