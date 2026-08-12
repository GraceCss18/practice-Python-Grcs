# ============================================
# EJERCICIOS - Listas en Python
# Escribe tu código debajo de cada enunciado
# ============================================

# --------------------------------------------
# ACTIVIDAD 1: Explica con tus palabras qué hace 
# cada línea, agregando un comentario arriba de cada una
# --------------------------------------------

# notas = []
#es para crear una caja vacia, en este caso se llama notas, donde se guardaran numeros

# nota1 = float(input("Ingresa una nota: "))
#agrego los numeros dentro de la caja

# notas.append(nota1)
# print(f"Total de notas: {notas}")
#muestro en pantalla el contenido de la caja mas un mensaje


# --------------------------------------------
# EJERCICIO 1
# Crea una lista vacía llamada "temperaturas".
# Pide 3 temperaturas al usuario (una por una) y 
# agrégalas a la lista. Al final, imprime la temperatura 
# más alta y la más baja (usa max() y min())
# --------------------------------------------
temperaturas = []
for i in range(3):  
    temp = float(input("Ingresa una temperatura: "))  
    temperaturas.append(temp)  

print("La más alta es:", max(temperaturas))  
print("La más baja es:", min(temperaturas))  


# --------------------------------------------
# EJERCICIO 2
# Crea una lista con 5 nombres de compañeros.
# Recorre la lista e imprime cada nombre con un saludo, 
# ejemplo: "Hola, Juan!"
# --------------------------------------------
nombres = ["Juan", "María", "Pedro", "Ana", "Luis"]  

for nombre in nombres:  
    print(f"Hola, {nombre}!")  



# --------------------------------------------
# RETO OPCIONAL (para quien quiera ir más allá)
# Usando list comprehension, crea una lista nueva 
# que contenga solo las temperaturas mayores a 20 grados 
# de tu lista "temperaturas" del Ejercicio 1
# --------------------------------------------
calientes = []
for temp in temperaturas:
    if temp > 20:
        calientes.append(temp)