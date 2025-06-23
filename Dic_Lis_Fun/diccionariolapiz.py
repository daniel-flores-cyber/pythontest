productos={
    "lapiz": 100,
    "goma": 100,
    "estuche": 500,
    "plumon": 1000
}

while True:
    while True:
        try:
            print('''
1.- agregar articulos y precio
2.- ver listado
3.- borrar articulo
4.- actualizar precio
5.- salir''')
            op=int(input("seleccione una opcion "))
            break
        except Exception:
            print("ERROR")
    match op:
        case 1:
            art=input("ingrese el nombre del articulo ")
            precio=input("ingrese el precio de articulo ")
            productos[art]=precio
        case 2:
            for nom, precio in productos.items():
                print(nom,"$",precio)
        case 3:
            for nom, precio in productos.items():
                print(nom,"$",precio)
            borrar=input("cual es el articulo que desea borrar ")
            del productos[borrar]
            print("el articulo",borrar,"fue borrado")
        case 4:
            for nom, precio in productos.items():
                print(nom,"$",precio)
            art=input("Cual es el articulo cuyo precio desea actualizar? ")
            if art in productos:
                precio=int(input("ingrese el precio nuevo: "))
                productos[art]=precio
            else:
                print("el articulo no existe")
        case 5:
            print("saliendo")
            break
        case _:
            print("opcion invalida")                
                               
    
