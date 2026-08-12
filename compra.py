#Ejercicio 2:** Una tienda da un premio si el cliente compra 5 productos o más. 
# Escribe los pasos para decidir si aplica el premio.

#Pseudocodigo:
#Se crea la variable de la cantiad minima de compra para obetener el premio
#Se pregunta al cliente cual fue la cantidad de su compra
#Si el cliente alcanzo la minima o mas cantidad necesario obtiene el premip
#Si no se le enseña cuanto le falto para obtenerlo


minimoPremio = 5 
#usar el int porque es en numeros
productosComprados = int(input("¿Cuántos productos adquirio el día de hoy?"))

if productosComprados >= minimoPremio:
    print("¡Usted es el feliz ganador de un premio sopresa!")
else:
    #la f_string me permitio agregar variables y poder hacer una operacion con esas variables 
    print(f"Ups! Te faltaron : {minimoPremio - productosComprados} producto " )

