personas={
    1:{"nombre":"juan",
       "numero":12345,
       "contraseña":"AAss22"}
}
def valid_cont(clave):
    mayusculas=0
    minusculas=0
    digitos=0
    for palabra in clave:
        if palabra.isupper():
            mayusculas+=1
        if palabra.islower():
            minusculas+=1
        if palabra.isdigit():
            digitos+=1
    if mayusculas==2 and minusculas==2 and digitos==2 and len(clave)==6:
        print("clave ingresada")
        return True
    else:
        print("ERROR,intente nuevamente")
        return False

def mostrar(dic):
    for k,v in dic.items():
        print(k,v)

def ingresar(dic):
            nombre=input("ingrese el nombre ")
            numero=int(input("ingrese el numero "))
            contarseña=input("ingrese la contarseña ")
            if valid_cont(contarseña):
                print("correctamente")
                largo=list(personas.keys())[-1]
                personas[largo+1]={"nombre":nombre,"numero":numero,"contraseña":contarseña}
            else:
                print("la contraseña debe contener 2 mayusculas,2 minusculas y 2 digitos y largo 6")    

def act(dic):
            mostrar(dic)
            act=int(input("que personas desea actualizar "))
            while True:
                print('''
                      1.-nombre
                      2.-numero
                      3.-contraseña
                      4.-salir''')
                dato=int(input("ingrese una opcion"))
                match dato:
                    case 1:
                        n=input("ingrese el nuevo nombre ")
                        dic[act]["nombre"]=n
                    case 2:
                        n=int(input("ingrese el nuevo numero "))
                        dic[act]["numero"]=n
                    case 3:
                        n=input("ingreese la nueva contraseña ")
                        if valid_cont(n):
                            dic[act]["contraseña"]=n  
                        else:
                            print("la contraseña debe contener 2 mayusculas,2 minusculas y 2 digitos y largo 6")                
                    case 4:
                        break
                    case _:
                        print("opcion invalida")       

def borrar(dic):
     mostrar(dic)
     borrar=int(input("cual desea borrar "))
     del dic[borrar]
while True:
    print('''
          1.-ingresar persona
          2.-mostrar lista
          3.-actualizar
          4.-borrar
          5.-salir''') 
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            ingresar(personas)   
        case 2:
            mostrar(personas)
        case 3:
            act(personas)
        case 4:
            borrar(personas)
        case 5:
            print("saliendo")
            break
        case _:
            print("opcion invalida")         
