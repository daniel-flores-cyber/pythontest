carrito={
    1:{"producto":"manzana",
     "precio":500,
     "codigo":"Ma2"}
}
def valid_codigo(codi):
    mayuscula=False
    minuscula=False
    digito=False
    for palabra in codi:
        if palabra.isupper():
            mayuscula=True
        if palabra.islower():
            minuscula=True    
        if palabra.isdigit():
            digito=True
    if mayuscula and minuscula and digito and len(codi)==3:
        print("el codigo esta bien")
        return True
    else:
        print("ERROR, el codigo debe tener una mayuscula, una minuscula, un digito y un largo de 3")     
        return False       

def ingre_pro(dic):
            producto=input("ingrese el nombre del producto ")
            while True:
                try:
                    precio=int(input("ingrese el precio "))
                    break
                except Exception:
                    print("ingrese numeros enteros ")
            codigo=input("ingrese el codigo ")
            if valid_codigo(codigo):
                largo=list(dic.keys())[-1]
                dic[largo+1]={"producto":producto,"precio":precio,"codigo":codigo}
            else:
                print("intente nuevamente")

def mostrar(dic):
     for k,v in dic.items():
          print(k,v)

def act_ca(dic):
            mostrar(dic)
            act=int(input("que producto desea actualizar "))
            while True:
                 print('''
                       1.-nombre
                       2.-precio
                       3.-codigo
                       4.-salir''')
                 dato=int(input("ingrese una opcion "))
                 match dato:
                      case 1:
                           m=input("ingrese el nuevo nombre ")
                           dic[act]["producto"]=m
                      case 2:
                           m=int(input("ingrese el nuevo precio "))
                           dic[act]["precio"]=m
                      case 3:
                           m=input("ingrese el nuevo codigo ")
                           if valid_codigo(m):
                                print("codigo ingresado")
                                dic[act]["codigo"]=m   
                           else:
                                print("ERROR,, el codigo debe tener una mayuscula, una minuscula y un digito")
                      case 4:
                           break                 

def borrar_pro(dic):
            mostrar(dic)
            borrar=int(input("que producto desea borrar "))
            del dic[borrar]     
while True:
    print('''
          1.-ingresar producto
          2.-ver carrito
          3.-actualizar producto
          4.-borrar producto
          5.-salir''')
    op=int(input("ingrese una opcion "))
    match op:
        case 1:
            ingre_pro(carrito)
        case 2:  
            mostrar(carrito)  
        case 3:
            act_ca(carrito)
        case 4:
            borrar_pro(carrito)
        case 5:
              print("saliendo")
              break
        case _:
              print("opcion invalida")                   
              