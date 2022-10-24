# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

def promedio(numeros_fun):
    print("Funcion promedio")
    resultado = 0
    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:

    # promedio = sumatoria_numeros / cantidad_numeros

    # Resuelva la sumatoria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números
    cantidad_numeros = len(numeros_fun)
    sumatoria_numeros = sum(numeros_fun)
    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos)
    if cantidad_numeros == 0:
        resultado = 'Lista vacía. No es posible calcular promedio.'
    else:
        resultado = sumatoria_numeros / cantidad_numeros
    return resultado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 6, 8, 10, 12]

    # Alumno: Complete la función "promedio"

    # Llamar a la función en este lugar y capturar el valor del retorno
    result_prom = promedio(numeros)

    # Luego imprimir en pantalla el valor resultante:
    # print(....)
    print('El promedio de los elementos de la lista', numeros, 'es:', result_prom)
    print("terminamos")