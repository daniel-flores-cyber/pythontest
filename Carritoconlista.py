# crear carrito 3.0
# tomar el carrito de compras anterior y hacerlo con listas
# 1.-ingresar productos
# 2.-comprar
# 3.-crear boleta
# 4.-salir
# que el carrito comience con 3 productos
# hay que hacer 3 listas, productos, precio y carrito
# ------------------------------------------------------------------

productos=["disco ssd 1tb", "memoria ram 8gb", "mouse"]
precios=[70000, 30000, 15000]
carrito=[]

while True:
    print('''
1.- ingresar productos a la tienda
2.- comprar
3.- crear boleta
4.- salir''')
    op=int(input("ingrese una opcion: "))
    match op:
        case 1:
            pro=input("ingrese el nombre del producto: ")
            productos.append(pro)
            pre=int(input("ingrese el precio: "))
            precios.append(pre)
        case 2:
            for i in range(len(productos)):
                print(i+1, ".-", productos[i], "$", precios[i])
            pro=int(input("selecione que quiere comprar: "))
            carrito.append(pro-1)
            print("usted seleciono", productos[pro-1])
        case 3:
            total=0
            print("------0------")
            print("bienvenido a PC house")
            for i in carrito:
                print(productos[i],"--$",precios[i])
                total=total+precios[i]
                print("el total de articulos es", len(carrito))
                print(("su total es",total))
                print("su total mas iva es",total*1.19)
                print("-----0-----")
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion invalidad")            

        
