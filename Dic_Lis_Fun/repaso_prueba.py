juegos={
    1:{
        "nombre":"Metroid Dread",
        "precio": 50000,
        "code":"MMdd2023"
    },
    2:{
        "nombre":"Pikmin 4",
        "precio": 55000,
        "code":"pKMn2022"
    }
}
def valida_code(clave):
     mayusculas=0
     minusculas=0
     digito=0
     for palabra in clave:
          if palabra.isupper():
               mayusculas+=1
          if palabra.islower():
               minusculas+=1
          if palabra.isdigit():
               digito+=1
     if mayusculas==2 and minusculas==2 and digito==4:
          print("el codigo esta bien escrito")
          return True
     else:
          print("el codigo esta mal escrito")
          return False  
                    
def mostar_juegos(dic):
    for j,datos in dic.items():
                print(j,datos)

def agregar_juego(dic):
           nombre=input("ingrese el nombre ")
           precio=int(input("ingrese el precio "))
           code=input("ingrese el codigo ")
           if valida_code(code):
               largo=list(dic.keys())[-1]
               dic[largo+1]={
                     "nombre":nombre,
                     "precio":precio,
                     "code":code
           }
           else:
                print("el codigo es invalido, intente nuevamente")

def actu_juegos(dic):
      
      mostar_juegos(dic)
      act=int(input("seleccione el juego que deseas actualizar "))
      while True:
            print('''
                  1.-nombre
                  2.-precio
                  3.-code
                  4.-salir''')
            dato=int(input("que dato va a actualizar "))
            match dato:
                  case 1:
                     n=input("ingrese el nuevo nombre ")
                     dic[act]["nombre"]=n
                  case 2:
                     n=int(input("ingrese el nuevo precio "))
                     dic[act]["precio"]=n
                  case 3:
                     n=input("ingrese el nuevo codigo ")
                     if valida_code(n):
                           dic[act]["code"]=n
                     else:
                           print("el parametro del codigo es invalido")
                           print('''
                              el codigo debe tener, 2 mayusculas, 
                              2 minusculas y 4 numeros ''')
                  case 4:
                     break
                  case _:
                     print("opcion invalida") 

def borrar_juego(dic):
            mostar_juegos(dic)
            borrar=int(input("que juego desea borrar "))
            del dic[borrar]
while True:
    print('''
          1.-agregar juego
          2.-mostrar juego
          3.-actuallizar juego
          4.-borrar juego
          5.-salir''')
    op=int(input("selccione una opcion "))
    match op:
        case 1:
           agregar_juego(juegos)
        case 2:
            mostar_juegos(juegos)
        case 3:
            actu_juegos(juegos)             
        case 4:
            borrar_juego(juegos)
        case 5:
            print("saliendo")
            break    
        case _:
              print("opcion invalida")
            
                  