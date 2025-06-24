# nuevos diccionarios y manipulacion de datos
juegos={
    1:{"nombre":"metroid dread",
       "precio": 50000,
       "code":"MMdd2323"},
    2:{"nombre":"pikmin 4",
       "precio": 55000,
       "code":"PKmn2323"} 
}
# el codigo debe tener 2 mayusculas, 2 minusculas, y 4 numeros
def mostrar_juegos(dic):
   for j,datos in dic.items():
             print(j,datos)

while True:
    print('''
          1.-agregar producto
          2.-mostrar producto
          3.-actualizar producto
          4.-borrar producto
          5.-salir''')
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            nombre=input("ingrese el nombre ")
            precio=int(input("ingrese el precio "))
            code=input("ingrese el codigo ")
            
            largo=len(juegos)
            juegos[largo+1]={"nombre":nombre,
                    "precio":precio,
                    "code":code}
        case 2:
            mostrar_juegos(juegos)
        case 3:
            mostrar_juegos(juegos)
            act=int(input("seleccione el producto que desea actualizar "))
            while True:
               print('''
                     1.-actualizar nombre
                     2.-actualizar precio
                     3.-actualizar code
                     4.-salir''')
               dato=int(input("ingrese una opcion "))
               match dato:
                  case 1:
                     n=input("ingrese el nuevo nombre ")
                     juegos[act]=["nombre"]=n
                  case 2:   
                     n=int(input("ingrese el nuevo precio "))
                     juegos[act]=["precio"]=n
                  case 3:
                     n=input("ingrese el nuevo code ")
                     juegos[act]=["code"]=n  
                  case 4:
                     break
                  case _:
                     print("opcion invalida ")
        case 4:
            mostrar_juegos(juegos)             
        case 5:
          print("saliendo")
          break
        case _:
          print("opcion invalida")      
