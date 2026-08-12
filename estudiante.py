precio = 8000
#preguntar si es estudiante
es_Estudiante = input("¿Eres estudiante? (Si/No)").lower()
#debo usar el .lower para que las respuestas que de el usuario asi sean en matuscula, min, el codigo me lo lea 
#todo como min y que acepte toda las respuestas
# es_Estudiante = es_Estudiante.lower() 
# print(es_Estudiante) es para verificar si leia el lower
#recuerda usar los puntos en las condicionales
if es_Estudiante == "si":
    descuento = precio * 0.20
    precioFinal = precio - descuento
else:
    precioFinal = precio

print("Usted debe pagar: " + str(precioFinal))

