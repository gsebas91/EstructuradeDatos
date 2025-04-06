print("bienvenidos a mis estructuras de datos")

# estructura de datos = almacenan valores
# str, bool, numerico (int), float

# Listas, tuplas, conjuntos y diccionarios

# Variable simple
x = 9
y = 10
temp = 0
x = 18

#estructura de datos
# Lista:
numeros = [1, 2 , 3, 4, 5, 6, "Sebas", True, 10, 11, 1, 2]
# las listas son mutables.
# sí permiten valores duplicados

print(numeros)
numeros.append("Martinez")
print("====== después de agregar=====")
print(numeros)

print("====== después de meter un valor=====")
numeros[6] = 19
print(numeros)

print(numeros[6])
numeros.remove(2)
print("====== después de eliminar=====")
print(numeros)





# Tupla:
numeros_primos = (1, 2 , 3, 4, 5, 6, "Sebas", True, 10, 11)
# las tuplas son inmutables
# sí permiten valores duplicados

# Conjuntos:
numeros_nuevos = {1, 2 , 3, 4, 5, 6, "Sebas", True, 10, 11}

# Diccionarios:
persona = {
    "nombre": "Sebas Martinez",
    "edad": 24,
    "ciudad": "Lima",
    "Correo": "mzlgary@gmail.com"
}


