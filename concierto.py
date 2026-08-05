#concierto

edadUsurio = int(input("Ingrese su edad"))
print(f"edadUsuario : {edadUsurio}")

diasDeCompra = int(input("Ingrese la fecha de su compra"))
print(f"diasDeCompra : {diasDeCompra}")



if edadUsurio >= 18 and diasDeCompra >= 7:
    print(f"Tu entrada es VIP")
elif edadUsurio >= 18 or diasDeCompra >= 7:
    print(f"Tu entrada es general")
else:
    print(f"No tienes entrada")
    


