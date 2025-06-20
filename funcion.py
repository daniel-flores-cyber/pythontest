# definir con argumento
# def suma():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("ingrese un numero "))
#     print(n1+n2)

# def suma_arg(n1, n2):
#     print(n1+n2)
# # -----------------------

# # retornar
# def suma_ret():
#     n1=int(input("ingrese un numero "))
#     n2=int(input("ingrese un numero "))
#     return n1+n2
# print(suma_ret())
# # ------------------------
# # argumento y retorno
# def suma_arg_ret(n1,n2):
#     return n1+n2
# print(suma_arg_ret(10,40))
# ------------------------------------------------

# realizar una funcion que calcule el IVA
# realizar una funcion que calcule el descuento
# def iva(n):
#     return n*0.19
# neto=5000
# print("el iva es", iva(neto))
# print("el precio total es",iva(neto)+neto)
     
# def cal_desc(precio, porc):
#     return precio+(porc/100)
# print(cal_desc(1000, 20))
# -----------------------------------------------
# diccionarios dentro de listas
productos=[
    {"nombre":"lapiz","precio":400},
    {"nombre":"goma","precio":200},
    {"nombre":"estuche","precio":1600}
]
for producto in productos:
    print("el precio del articulo",producto["nombre"],"es",producto["precio"])
while True:
    print('''
    1.-agregar articulo
    2.-borrar articulo
    3.-actualizar articulo
    4.-mostrar listado de articulos
    5.-salir''')
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            art=(input("ingrese el nombre del articulo "))
            pre=int(input("ingrese el precio del articulo "))
            productos.append({"nombre":art,"precio":pre})
        case 2:
            for n,producto in enumerate(productos):
                print(n+1,producto["nombre"],producto["precio"])
                borrar=int(input("selecciones cual desea borrar"))
                productos.pop(borrar)
        case 3:
            for n,producto in enumerate(productos):
                print(n+1,producto["nombre"],producto["precio"])
            act=int(input("seleccione cual desea actualizar"))
            nombre=input("ingrese el nombre del articulo ")
            precio=int(input("ingrese el nuevo precio "))
            productos[act-1]["nombre"]=nombre
            productos[act-1]["precio"]=precio
        case 4:
            for n,producto in enumerate(productos):
                print(n+1,producto["nombre"],producto["precio"])
        case 5:
            print("saliendo")
            break        
        case _:
            print("opcion invalida")

