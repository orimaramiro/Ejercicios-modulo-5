# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
# def generar_invitados():


# --------------------------------


cant_inv = 3
    
    # Alumno: Crear la función "generar_invitados"
def generar_inv():
    lista_inv = []
    for i in range (cant_inv):
        invitado = str (input("Agregue nombre de un invitado"))
        lista_inv.append(invitado)
    return lista_inv


    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    # lista_invitados = generar_invitados()

    # Imprimir en pantalla "lista_invitados":


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    lista_invitados = generar_inv()
    print(lista_invitados)

print("terminamos")
