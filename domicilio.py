#========================================
#en python los comentarios son con el # 
#sistema de domicilio - etapa    
#========================================

#vamsos a usar el while ahora

continuar = "s"

while continuar == "s":
    # Preguntamos la distancia y la convertimos a numero decimal
    distancia_km = float(input("Distancia del domicilio en km: "))

    # Evaluamos en que rango cae la distancia
    if distancia_km <= 3:
        costo = 3000
    elif distancia_km <= 8:
        costo = 7000
    else:
        costo = 0

    # Mostramos el resultado
    if costo == 0:
        print("Fuera de cobertura. No se puede realizar el domicilio.")
    else:
        print(f"Costo del domicilio: ${costo}")

    # Preguntamos si quiere calcular otro
    continuar = input("¿Calcular otro domicilio? (s/n): ")

print("Gracias por usar el sistema.")

#input funciona para motsrar el mensaje al usuario 
#float lo convierte en numeros con comas, para que lo pueda mostrar
#imprimir la variable
# Evaluar condiciones
#para crear  un nuevo  repositorio en githab es git init



        
