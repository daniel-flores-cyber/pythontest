# son conjuntos de pares de datos
#lista dentro de listas
# kilo=[
#     [3,4],
#     [9,8]
# ]
# print(kilo[1][1])
# ---------ejemplo----------------
# dic={
#     "nombre": "david finch",
#     "numero": 98765,
#     "casado": True
# }
# print(dic["nombre"])
# for key, value in dic.items():
#     print(key,value)
# -------------------------------------------   
# frutas={
#     "manzana": 1500,
#     "frutilla": 1600,
#     "durazno": 3800

# } 
# print(frutas)
# frutas["pera"]=1200
# print(frutas)   
# fru=input("ingrese la fruta ")
# val=int(input("ingrese el precio "))
# frutas[fru]=val
# print(frutas)
# -----------------------------------------------
# usando diccionario
# 1.- ingresar fruta
# 2.- actualizar precio
# 3.- borrar fruta y precio
# 4.- mostrar todas las frutas y precios
# 5.- salir

frutas={}
while True:
    print('''
    1.- ingresar fruta
    2.- actualizar precio
    3.- borrar fruta y precio
    4.- mostrar todas las frutas y precios
    5.- salir''')
    op=int(input("seleccione una opcion "))
    match op:
        case 1:
            fru=input("ingrese la fruta ")
            val=int(input("ingrese el valor "))
            frutas[fru]=val
        case 2:
            print()
        case 3:
            print()
        case 4:
            for key in frutas:
                print(key) 
        case 5:
            print("saliendo")
            break
        case _:
            print("opcion invalida ")               
            