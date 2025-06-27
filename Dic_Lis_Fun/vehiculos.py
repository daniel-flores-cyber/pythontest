# '''
# Crear gestion de vehiculos
# Crear programa para un parking de autos
# se debe ingresar
# Marca, año, patente, Tipo

# Marca: tipo string, se debe tipear la marca
# año: tipo int , solo de 4 digitos enteros
# patente: debe tener 4 letras minusculas y 2 digitos
# tipo: S= sedan, C= Camioneta, M= moto

# Se deve validar cada aspecto y tener un mantenedor para 
# todos los vehiculos motorizados

# 1.- Ingresar Vehiculo
# 2.- Mostrar Vehiculos
# 3.- Actualizar Vehiculo
# 4.- Borrar Vehiculo
# 5.- Mostar estadisticas: ultimo vehiculo ingresado, y total en garage
# 6.- Salir

# Usar dunciones con argumentos para poder validar
# y para poder llamar las acciones dentro del menu
# '''
vehiculos={
    1:{"marca":"nissan",
     "año":2005,
     "patente":"fghj22",
     "tipo":"s"}
}
def valid_pat(pat):
    minusculas=0
    digitos=0
    for palabra in pat:
        if palabra.islower():
            minusculas+=1
        if palabra.isdigit():
            digitos+=1
    if minusculas==4 and digitos==2:
        print("el codigo esta bien escrito")
        return True
    else:
        print("el codigo esta mal escrito")  
        return False

def ingre_ve(dic):
            marca=input("ingrese la marca ")
            while True:
                try:
                    año=int(input("ingrese el año "))
                    break
                except Exception:
                  print("ERROR, debe ingresar numero enteros")    
            patente=input("ingrese la patente ")
            if valid_pat(patente):
                tipo=input('''
                        s=sedan
                        c=camioneta
                        m=moto
                        ''')
                largo=list(vehiculos.keys())[-1]
                vehiculos[largo+1]={"marca":marca,"año":año,"patente":patente,"tipo":tipo}
            else:
                print("el codigo es invalido, intente nuevamente ")      

def mostrar(dic):
    for k,v in dic.items():
        print(k,v)

def act_ve(dic):
            mostrar(dic)
            dato=int(input("que vehiculo desea actualizar "))
            while True:
                print("que desea actualizar")
                opcion=int(input('''
                                 1.-marca
                                 2.-año
                                 3.-patente
                                 4.-tipo
                                 5.-salir
                                 '''))
                match opcion:
                    case 1:
                        m=input("ingrese la nueva marca ")
                        dic[dato]["marca"]=m
                    case 2:
                        while True:
                            try:
                                m=int(input("ingrese el nuevo año ")) 
                                break   
                            except Exception:
                                print("solo numeros enteros")
                        dic[dato]["año"]=m  
                    case 3:
                        m=input("ingrese la nueva patente ")
                        if valid_pat(m):
                            print("ingresada correctamente")
                            dic[dato]["patente"]=m
                        else:
                            print("el codigo es invalido, intente nuevamente ") 
                    case 4:
                        m=input("ingrese el nuevo tipo ")
                        dic[dato]["tipo"]=m
                    case 5:
                        break
                    case _:
                        print("opcion invalida") 

def borar_ve(dic):
            mostrar(dic)
            borrar=int(input("que vehiculo desea borrar ")) 
            del dic[borrar]  
while True:
    print('''
          1.-ingresar vehiculo
          2.-mostrar vheiculo
          3.-actualizar vehiculo
          4.-borrar vehiculo
          5.-salir''')
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            ingre_ve(vehiculos)
        case 2:
            mostrar(vehiculos)
        case 3:
            act_ve(vehiculos)
        case 4:
            borar_ve(vehiculos)
        case 5:
            print("saliendo")
            break
        case _:
              print("opcion invalida") 

    