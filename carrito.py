pro=int
suma=0
art=0
nombre=str(input("ingrese su nombre "))
while pro!=5:
    print("Productos")
    print("1.-arroz $1000")
    print("2.-fideos $1500")
    print("3.-atun $700")
    print("4.-aceite $2000")
    print("5.-Salir")
    try:
        pro=int(input())

        match pro:
            case 1:
                suma=suma+1000
                art=art+1
            case 2:
                suma=suma+1500
                art=art+1

            case 3:
                suma=suma+700
                art=art+1

            case 4:
                suma=suma+2000  
                art=art+1
    except Exception:
        print("Solo puede ingresar numeros enteros")
 
total=suma
print("hola",nombre)
print("El total es",total)
print("El total con iva es",total*1.19)
print("cantidad de articulos",art)
                   


