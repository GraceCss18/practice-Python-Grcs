# Ejercicio 3:** Un semáforo cambia de color cada cierto tiempo. Si está en rojo, los carros paran; si está en verde, avanzan;
#  si está en amarillo, deben ir despacio. Escribe los pasos para esta lógica.

colorSemaforo = input("¿De que color es el semaforo?: ")

if colorSemaforo == "rojo":
    print("¡Debes parar!")
elif colorSemaforo == "amarillo":
    print("Debes ir despacio")
else:
    colorSemaforo == "verde"
    print("Puedes avanzar")

