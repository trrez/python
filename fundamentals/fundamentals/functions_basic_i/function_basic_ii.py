def cuenta_regresiva(num):
    lista = []
    for x in range(num + 1):
        lista.append(x)
    lista.reverse()
    return lista


resultado = cuenta_regresiva(5)
print(resultado)


def imprimir_y_devolver(lista):
    for x in range(len(lista)):
        if lista[x] == lista[0]:
            print(lista[0])
    return lista[1]


resultado_imprimir_y_devolver = imprimir_y_devolver([1, 2])
print(resultado_imprimir_y_devolver)


def primero_mas_largo(lista):
    for x in range(len(lista)):
        if lista[x] == lista[0]:
            return lista[x] + len(lista)


resultado_primero_mas_largo = primero_mas_largo([1, 2, 3, 4, 5])
print(resultado_primero_mas_largo)


def valores_mayores_que_el_segundo(lista):
    valores_mayores = []
    length_lista = 0

    if len(lista) < 2:
        return False

    for x in range(len(lista)):
        if lista[x] > lista[1]:
            valores_mayores.append(lista[x])
            length_lista += 1
    print(length_lista)
    return valores_mayores


resultado_valores_mayores = valores_mayores_que_el_segundo([5, 2, 3, 2, 1, 4])
print(resultado_valores_mayores)

resultado_valores_mayores2 = valores_mayores_que_el_segundo([5])
print(resultado_valores_mayores2)


def lenght_value(num, num2):
    lista = []
    for x in range(num):
        lista.append(num2)
    return lista


resultado_lengh = lenght_value(4, 7)
print(resultado_lengh)

resultado_lengh2 = lenght_value(6, 2)
print(resultado_lengh2)
