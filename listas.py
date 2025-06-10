# uso y ejemplos de lista
# que es una lista?
# una numeros es una coleccion de datos

# numeros=[3,6,2,88,45]
# #      0 1 2  3   4

# # print(numeros)

# # numeros.append(64)
# # print(numeros)

# # for numero in numeros:
# #     print("nota:",numero*3)
# num=int(input("ingrese un num "))
# numeros.append(num)
# print(numeros)

nombres=[]
apellidos=[]
while True:
    print('''
          1.-ingresar nombre y apellido
          2.-buscar nombre
          3.-mostrar nombres y apellidos
          4.-salir
          ''')
    op=int(input("seleccione una opcion "))
    match op:
        case 1:
            nom=input("ingrese un nombre ")
            nombres.append(nom)
            ape=input("ingrese un apellido ")
            apellidos.append(ape)
            # print(nombres)
        case 2:
            busca=input("ingrese el nombre a buscar ")
            if busca in nombres:
                print("el nombre",busca,"existe en la lista")
            else:
                print("el nombre",busca,"no existe en la lista")    
        case 3:
            for i in range(len(nombres)):
                print(i+1,".-",nombres[i],apellidos[i])    
        case 4:
            print("saliendo") 
            break       
        case _:
            print("opcion invalida")
