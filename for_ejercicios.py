# ============================================
# GUÍA Y EJERCICIOS - For y List Comprehension
# ============================================

# --------------------------------------------
# RECORDATORIO: ¿QUÉ ES UN FOR?
# Recorre una lista, elemento por elemento, y 
# repite un bloque de código para cada uno
# ------------------------------------------

# ============================================
# NIVEL BÁSICO
# ============================================

# Ejercicio 1: Recorre la lista "colores" e imprime cada uno 
# con el formato "Color: nombre"
#colores = ["rojo", "azul", "verde", "amarillo"]

colores = ["amarillo", "azul", "rojo", "violeta", "carmesi", "verde"]
for color in colores:
    print(f"Color: {color}")

print("-----------------------------------------------")


#==============================================
# Ejercicio 2: Recorre la lista "precios" y calcula el total 
# (suma de todos)
#precios = [15000, 22000, 8000, 35000]

precios = [15000, 22000, 8000, 35000]
total = 0
for precio in precios:
    total = total + precio

print(total)
print("-----------------------------------------------")


# Ejercicio 3: Recorre la lista "edades" y cuenta cuántas 
# personas son mayores de edad (18 o más)

edades = [15, 22, 17, 30, 12, 19]
contador = 0
#debo inciar el contador desde 0

for edad in edades:
    if edad >= 18:
        contador = contador + 1

print(contador)
print("-----------------------------------------------")


# Ejercicio 4: Recorre la lista "notas" y encuentra la nota 
# más alta SIN usar la función max()

notas = [3.5, 4.2, 2.8, 4.8, 3.9]
notaMasAlta = notas[0]
for nota in notas:
    if nota > notaMasAlta:
        notaMasAlta = nota

print(f"La nota mas alta es: {notaMasAlta}")
print("-----------------------------------------------")

# Ejercicio 5: Crea una nueva lista "dobles" que contenga cada 
# número de "numeros_base" multiplicado por 2

numeros_base = [1, 2, 3, 4, 5]
#para poder crear una la lista doble debo abir una nueva pero vacia
dobles = []
for numero in numeros_base:
    dobles.append( numero * 2) 
    #.append es para agregar elementos en un lista 

print(dobles)
print("-----------------------------------------------")

# ============================================
# NIVEL INTERMEDIO
# ============================================

# Ejercicio 6: Cuenta cuántas veces aparece el valor "manzana" 
# en la lista "frutas_repetidas"

frutas_repetidas = ["manzana", "pera", "manzana", "uva", "manzana"]
contador = 0

for fruta in frutas_repetidas:
    if fruta == "manzana":
        contador = contador + 1

print(contador)
print("-----------------------------------------------")


# Ejercicio 7: Separa la lista "numeros_mixtos" en dos listas 
# nuevas: "pares" e "impares"

numeros_mixtos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
impares = []

for numero in numeros_mixtos:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(pares)
print(impares)
print("-----------------------------------------------")

# Ejercicio 8: Invierte el orden de la lista "orden_original"
# Pista: pueden usar .reverse(), slicing [::-1], o investigar 
# la función .insert() para hacerlo manualmente

orden_original = ["a", "b", "c", "d", "e"]
invertido = orden_original[::-1]
print(invertido)
print("-----------------------------------------------")

# Ejercicio 9: Combina "lista_a" y "lista_b" en una sola lista 
# nueva llamada "combinada"
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
#la forma mas larga en python
# combinada = []
# for numero in lista_a:  
#     combinada.append(numero)  

# for numero in lista_b:  
#     combinada.append(numero)  

# print(combinada)  # [1, 2, 3, 4, 5, 6]

#la mas rapida es sumarla ya que python lo permite
combinada = lista_a + lista_b  
print(combinada)  